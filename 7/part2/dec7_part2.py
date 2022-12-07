import sys
import os
f = open(os.path.join(sys.path[0], './../data.txt'), 'r')
lines = [l.rstrip() for l in f.readlines()]

class File:
    def __init__(self, name, size, parent):
        self._name = name
        self._size = size
        self._parent = parent
    
    def getSize(self):
        return self._size
    
    def getParent(self):
        return self._parent
    
    def getName(self):
        return self._name
    
    def __str__(self):
        return "{} -> {}".format(self._name, self._size)

class Dir:
    def __init__(self, name, parent):
        self._name = name
        self._files = []
        self._dirs = []
        self._parent = parent
    
    def getSize(self):
        size = 0
        for f in self._files:
            size += f.getSize()
        for d in self._dirs:
            size += d.getSize()
        return size
    
    def cd(self, dName):
        for d in self._dirs:
            if d.getName() == dName:
                return d
    
    def addDir(self, dir):
        self._dirs.append(dir)
    
    def getDirs(self):
        return self._dirs
    
    def addFile(self, file):
        self._files.append(file)

    def getParent(self):
        return self._parent
    
    def getName(self):
        return self._name
    
    def __str__(self, lvl=0):
        s = "dir {} -> \n".format(self._name)
        for d in self._dirs:
            s += "   "*(lvl+1) + d.__str__(lvl+1)
        for f in self._files:
            s += "   "*lvl + "   {} -> {}\n".format(f.getName(), f.getSize())
        return s


graph = Dir('/', None) # root
currentDir = graph

def parseInput():
    global currentDir
    i=1
    while i<len(lines): # for each line except the first one
        l=lines[i].split()
        if l[0] == '$': # command line
            if l[1] == 'ls': # if we're about to list dir
                i+=1
                l=lines[i].split()
                while i<len(lines): # until next command line
                    l=lines[i].split()
                    if l[0] == '$':# we have reach the next command line
                        break
                    if l[0] == 'dir':
                        newDir = Dir(l[1], currentDir)
                        currentDir.addDir(newDir)
                    else:
                        newFile = File(l[1], int(l[0]), currentDir)
                        currentDir.addFile(newFile)
                    i+=1
            elif l[1] == 'cd': # if we're about to change directory
                if l[2] == '..':
                    currentDir = currentDir.getParent()
                else:
                    currentDir = currentDir.cd(l[2])
                i+=1

parseInput()

TOTAL_SIZE = 70000000
NEEDED_SPACE = 30000000
USED_SPACE = graph.getSize()
UNUSED_SPACE = TOTAL_SIZE - USED_SPACE

SHOULD_DELETE = NEEDED_SPACE - UNUSED_SPACE

size = 0
smallestDir = None
dirs = [graph]
while len(dirs) != 0:
    d=dirs[0]
    dirs = dirs[1:]
    dirSize = d.getSize()
    if dirSize >= SHOULD_DELETE and (smallestDir==None or dirSize<smallestDir.getSize()):
        smallestDir = d
    dirs += d.getDirs()
print(smallestDir.getSize())
