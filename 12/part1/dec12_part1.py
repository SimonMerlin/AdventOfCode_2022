import sys
import os
f = open(os.path.join(sys.path[0], './../data.txt'), 'r')
lines = [l.rstrip() for l in f.readlines()]

class Point:
    def __init__(self, coordinates, cost, height):
        self.coordinates = coordinates
        self.cost = cost
        self.height = height
    
    def __str__(self):
        return "(coord : {}, cost: {}, height: {})".format(self.coordinates, self.cost, self.height)
    
    def __repr__(self) -> str:
        return self.__str__()

visitedPoints = dict()
currentPosition = None

ALPHABET = 'abcdefghijklmnopqrstuvwxyz'
start = None
arrival= None
costToArrival = None

def findStartAndArrival():
    global currentPosition, arrival
    r, c = 0, 0
    for r in range(len(lines)):
        for c in range(len(lines[0])):
            if lines[r][c] == 'S':
                lines[r] = lines[r][:c] + 'a' + lines[r][c+1:]
                currentPosition = Point((r,c), 0, 'a')
            if lines[r][c] == 'E':
                arrival = (r,c)
                lines[r] = lines[r][:c] + 'z' + lines[r][c+1:]

def computePossiblePaths(pointFrom):
    paths = []
    # UP
    coord = pointFrom.coordinates
    if coord[0]-1 >=0 and lines[coord[0]-1][coord[1]]!=start and ALPHABET.index(lines[coord[0]-1][coord[1]]) <= (ALPHABET.index(lines[coord[0]][coord[1]])+1):
        paths.append(Point((coord[0]-1, coord[1]), pointFrom.cost+1, lines[coord[0]-1][coord[1]]))
    #DOWN
    if coord[0]+1 < len(lines) and lines[coord[0]+1][coord[1]]!=start and ALPHABET.index(lines[coord[0]+1][coord[1]]) <= (ALPHABET.index(lines[coord[0]][coord[1]])+1):
        paths.append(Point((coord[0]+1, coord[1]), pointFrom.cost+1, lines[coord[0]+1][coord[1]]))
    #LEFT
    if coord[1]-1 >=0 and lines[coord[0]][coord[1]-1]!=start and ALPHABET.index(lines[coord[0]][coord[1]-1]) <= (ALPHABET.index(lines[coord[0]][coord[1]])+1):
        paths.append(Point((coord[0], coord[1]-1), pointFrom.cost+1, lines[coord[0]][coord[1]-1]))
    #RIGHT
    if coord[1]+1 < len(lines[0]) and lines[coord[0]][coord[1]+1]!=start and ALPHABET.index(lines[coord[0]][coord[1]+1]) <= (ALPHABET.index(lines[coord[0]][coord[1]])+1):
        paths.append(Point((coord[0], coord[1]+1), pointFrom.cost+1, lines[coord[0]][coord[1]+1]))
    
    return paths


findStartAndArrival()
points = [currentPosition]
visitedPoints[currentPosition.coordinates] = currentPosition
while len(points) != 0:
    currentPosition = points[0]
    points = points[1:]
    possiblesPoints = computePossiblePaths(currentPosition)
    for p in possiblesPoints:
        if p.coordinates in visitedPoints and p.cost < visitedPoints[p.coordinates].cost:
            visitedPoints[p.coordinates] = p
            points.append(p)
        elif not p.coordinates in visitedPoints:
            visitedPoints[p.coordinates] = p
            points.append(p)
        
        if p.coordinates == arrival and (costToArrival == None or costToArrival > p.cost):
            costToArrival = p.cost

print(visitedPoints)
print(costToArrival)