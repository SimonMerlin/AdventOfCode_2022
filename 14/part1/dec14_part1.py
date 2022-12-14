import sys
import os
import time
f = open(os.path.join(sys.path[0], './../data.txt'), 'r')
lines = [l.rstrip() for l in f.readlines()]

blocks = []

def buildAllBlocks():
    global blocks
    for l in lines:
        points = [p.split(",") for p in l.split(" -> ")]
        for i in range(len(points)):
            p = [int(x) for x in points[i]]
            if i != len(points)-1:
                blocks.append((p[0], p[1]))
                nextP = [int(x) for x in points[i+1]]
                if p[0] == nextP[0]: #same distance to the right => same column => vertical
                    if p[1]<nextP[1]:
                        for x in range(p[1]+1, nextP[1]):
                            blocks.append((p[0], x))
                    else:
                        for x in range(nextP[1]+1, p[1]):
                            blocks.append((p[0], x))
                else : #same distance to the top => same row => horizontal
                    if p[0]<nextP[0]:
                        for x in range(p[0]+1, nextP[0]):
                            blocks.append((x, p[1]))
                    else:
                        for x in range(nextP[0]+1, p[0]):
                            blocks.append((x, p[1]))
            else:
                blocks.append((int(p[0]), int(p[1])))

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
            elif (c, r) in blocks:
                row+='#'
            else:
                row+='.'
        _map.append(row)
    for r in _map:
        print(r)
    print('~~~~~~~~~~~~~~~~~~~~~~~~')

def fallIntoEndlessVoid(point):
    return point[0] > maxC or point[0] < minC or point[1] > maxR+2


def findLimits():
    minR, maxR, minC, maxC = blocks[0][1], blocks[0][1], blocks[0][0], blocks[0][0]
    for b in blocks[1:]:
        if b[0] < minC:
            minC = b[0]
        if b[0] > maxC:
            maxC = b[0]
        if b[1] < minR:
            minR = b[1]
        if b[1] > maxR:
            maxR = b[1]
    return minR, maxR, minC, maxC

sandUnitStartPoint = (500, 0)
sandUnitPosition = sandUnitStartPoint
sandUnitRestCounter = 0

def simulateSand():
    global blocks, sandUnitStartPoint, sandUnitPosition, sandUnitRestCounter
    while not fallIntoEndlessVoid(sandUnitPosition):
        if not (sandUnitPosition[0], sandUnitPosition[1]+1) in blocks: #position free verticaly
            print("DOWN")
            sandUnitPosition = (sandUnitPosition[0], sandUnitPosition[1]+1)
        elif not (sandUnitPosition[0]-1, sandUnitPosition[1]+1) in blocks:
            print("LEFT")
            sandUnitPosition = (sandUnitPosition[0]-1, sandUnitPosition[1]+1) # try go left
        elif not (sandUnitPosition[0]+1, sandUnitPosition[1]+1) in blocks:
            print("RIGHT")
            sandUnitPosition = (sandUnitPosition[0]+1, sandUnitPosition[1]+1) # try go right
        else: # sand unit blocked
            blocks.append(sandUnitPosition)
            sandUnitRestCounter += 1
            sandUnitPosition = sandUnitStartPoint
        printMap()


start = time.perf_counter()

buildAllBlocks()
minR, maxR, minC, maxC = findLimits() 
print("Please wait while computing... it may takes some times")
simulateSand()
end = time.perf_counter()

print(sandUnitRestCounter)
print(f"Execute code in {end - start:0.4f} seconds")