import sys
import os
import math
f = open(os.path.join(sys.path[0], './../data.txt'), 'r')
lines = [l.rstrip() for l in f.readlines()]

class Point:
    def __init__(self, r, c):
        self.r = r
        self.c = c
    
    def __hash__(self):
        return hash((self.r, self.c))

    def __eq__(self, other):
        if not isinstance(other, type(self)): return NotImplemented
        return self.r == other.r and self.c == other.c
    
    def __str__(self):
        return "[ {}, {} ]".format(self.r, self.c)
    
    def __repr__(self):
        return str(self)


class Knot:
    def __init__(self):
        self._position = Point(0, 0)
        self._visitedPoints = set()
        self._visitedPoints.add(self._position)
        self._child = None
    
    def setChild(self, child):
        self._child = child
    
    def getChild(self):
        return self._child

    def getPosition(self):
        return self._position

    def move(self, direction):
        if direction=='R':
            self._position = Point(self._position.r, self._position.c+1)
        elif direction=='L':
            self._position = Point(self._position.r, self._position.c-1)
        elif direction=='U':
            self._position = Point(self._position.r-1, self._position.c)
        elif direction=='D':
            self._position = Point(self._position.r+1, self._position.c)
    
    def join(self, position):
        # if overlap or already touching
        if abs(self._position.c - position.c)<=1 and abs(self._position.r - position.r)<=1:
            return
        # if in the same column
        elif  self._position.c == position.c:
            if position.r < self._position.r:
                self.move('U')
            else:
                 self.move('D')
        # if in the same row
        elif  self._position.r == position.r:
            if position.c < self._position.c:
                self.move('L')
            else:
                 self.move('R')
        #move diagonnaly
        else:
            if self._position.r<position.r and self._position.c<position.c:
                self.move('D')
                self.move('R')
            elif self._position.r>position.r and self._position.c<position.c:
                self.move('U')
                self.move('R')
            elif self._position.r<position.r and self._position.c>position.c:
                self.move('D')
                self.move('L')
            elif self._position.r>position.r and self._position.c>position.c:
                self.move('U')
                self.move('L')
        self._visitedPoints.add(self._position)

    
    def countVisitedPoints(self):
        return len(self._visitedPoints)

h = Knot()
childCreated = 0

def processMove(direction, times):
    global h, childCreated
    for _ in range(times):
        h.move(direction)
        parent = h
        child = h.getChild()
        while child != None:
            child.join(parent.getPosition())
            parent = child
            child = child.getChild()
        if childCreated<9:
            newChild = Knot()
            parent.setChild(newChild)
            childCreated+=1


for l in lines:
    l = l.split()
    processMove(l[0], int(l[1]))

parent = h
while parent.getChild() != None:
    parent = parent.getChild()

print(parent.countVisitedPoints())
