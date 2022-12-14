import sys
import os
import time
import copy
f = open(os.path.join(sys.path[0], './../data.txt'), 'r')
lines = [l.rstrip() for l in f.readlines()]

blocks = dict() #key = column, value = list of index of used rows
initialBlocks = dict()

def buildAllBlocks():
    global blocks, initialBlocks
    for l in lines:
        points = [p.split(",") for p in l.split(" -> ")]
        for i in range(len(points)):
            p = [int(x) for x in points[i]]
            if i != len(points)-1:
                if not p[0] in blocks:
                    blocks[p[0]] = []
                blocks[p[0]].append(p[1])
                nextP = [int(x) for x in points[i+1]]
                if p[0] == nextP[0]: #same distance to the right => same column => vertical
                    if p[1]<nextP[1]:
                        for x in range(p[1]+1, nextP[1]):
                            blocks[p[0]].append(x)
                    else:
                        for x in range(nextP[1]+1, p[1]):
                            blocks[p[0]].append(x)
                else : #same distance to the top => same row => horizontal
                    if p[0]<nextP[0]:
                        for x in range(p[0]+1, nextP[0]):
                            if not x in blocks:
                                blocks[x] = []
                            blocks[x].append(p[1])
                    else:
                        for x in range(nextP[0]+1, p[0]):
                            if not x in blocks:
                                blocks[x] = []
                            blocks[x].append(p[1])
            else:
                if not p[0] in blocks:
                    blocks[p[0]] = []
                blocks[p[0]].append(p[1])

    initialBlocks = copy.deepcopy(blocks)

def printMap():
    global sandUnitPosition
    _map=[]
    for r in range(0, maxR+1):
        row = str(r) + ' '
        if r < 10:
             row += ' '
        for c in range(minC, maxC+1):
            if (c, r) == sandUnitPosition:
                row+='+'
            elif c in blocks and r in blocks[c] and c in initialBlocks and r in initialBlocks[c]:
                row+='#'
            elif c in blocks and r in blocks[c]:
                row+='o'
            else:
                row+='.'
        _map.append(row)
    for r in _map:
        print(r)
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')

def isOnTheFloor(point):
    global floor
    return point[1]+1 == floor

def isBlocked(p):
    global blocks
    blockdown = p[0] in blocks and p[1]+1 in blocks[p[0]]
    blockLeft = p[0]-1 in blocks and p[1]+1 in blocks[p[0]-1]
    blockRight = p[0]+1 in blocks and p[1]+1 in blocks[p[0]+1]
    return blockdown and blockLeft and blockRight

def alreadyTaken(point):
    if not point[0] in blocks:
        return False
    return point[1] in blocks[point[0]]

def findLimits():
    minR, maxR, minC, maxC = None, None, None, None
    for c in blocks:
        if minC==None or minC > c:
            minC= c
        if maxC==None or maxC < c:
            maxC= c
        for r in blocks[c]:
            if minR==None or minR > r:
                minR= r
            if maxR==None or maxR < r:
                maxR= r
    return minR, maxR, minC, maxC

sandUnitStartPoint = (500, 0)
sandUnitPosition = sandUnitStartPoint
sandUnitRestCounter = 0

def simulateSand():
    global blocks, sandUnitStartPoint, sandUnitPosition, sandUnitRestCounter, floor
    while not (isBlocked(sandUnitPosition) and sandUnitPosition==sandUnitStartPoint):
        if not alreadyTaken((sandUnitPosition[0], sandUnitPosition[1]+1)) and not isOnTheFloor(sandUnitPosition): #position free verticaly
            sandUnitPosition = (sandUnitPosition[0], sandUnitPosition[1]+1)
        elif not alreadyTaken((sandUnitPosition[0]-1, sandUnitPosition[1]+1)) and not isOnTheFloor(sandUnitPosition):
            sandUnitPosition = (sandUnitPosition[0]-1, sandUnitPosition[1]+1) # try go left
        elif not alreadyTaken((sandUnitPosition[0]+1, sandUnitPosition[1]+1)) and not isOnTheFloor(sandUnitPosition):
            sandUnitPosition = (sandUnitPosition[0]+1, sandUnitPosition[1]+1) # try go right
        else: # sand unit blocked
            if not sandUnitPosition[0] in blocks:
                blocks[sandUnitPosition[0]] = []
            blocks[sandUnitPosition[0]].append(sandUnitPosition[1])
            sandUnitRestCounter += 1
            sandUnitPosition = sandUnitStartPoint
    sandUnitRestCounter += 1 # add the last sans unit blocked on top

start = time.perf_counter()

buildAllBlocks()
minR, maxR, minC, maxC = findLimits()
floor = maxR+2
maxR= floor
minC -=10
maxC +=10
printMap()
print("Please wait while computing... it may takes some times")
simulateSand()
end = time.perf_counter()

print(sandUnitRestCounter) 
print(f"Execute code in {end - start:0.4f} seconds")