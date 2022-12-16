import sys
import os
import re
f = open(os.path.join(sys.path[0], './../data.txt'), 'r')
lines = [l.rstrip() for l in f.readlines()]

takenPoints = dict() # key = row, value = list of taken column in this row
sensors = []
beacons = []
takenPointsByBeacon = dict()

ROW = 2000000

class Point():
    def __init__(self, x, y, type, beacon):
        self.x = x 
        self.y = y
        self.type = type
        self.closestBeacon = beacon


def manhattanD(p1, p2):
    return abs(p1.x-p2.x) + abs(p1.y-p2.y) 

def getAllPointInsideManhattanFrom(point, d):
    if point.y-d<=ROW and point.y+d>=ROW:
        dy = abs(point.y - ROW)
        for x in range(point.x-(d-dy), point.x+(d-dy)+1):
            if not ROW in takenPoints:
                takenPoints[ROW] = set()
            takenPoints[ROW].add(x)

def parseInput():
    global sensors, beacons, takenPointsByBeacon
    for l in lines:
        sx, sy, bx, by = re.findall('\d+', l)
        beacon = Point(int(bx), int(by), 'B', None)
        if not by in takenPointsByBeacon:
            takenPointsByBeacon[int(by)] = set()
        takenPointsByBeacon[int(by)].add(int(bx))
        beacons.append(beacon)
        sensors.append(Point(int(sx), int(sy), 'S', beacon))


parseInput()

for sensor in sensors:
    getAllPointInsideManhattanFrom(sensor, manhattanD(sensor, sensor.closestBeacon))

takenPointWithBeacons = [y for y in takenPoints[ROW] if not ROW in takenPointsByBeacon or not y in takenPointsByBeacon[ROW]]
print(len(takenPointWithBeacons))