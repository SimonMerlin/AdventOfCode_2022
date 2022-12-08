import sys
import os
f = open(os.path.join(sys.path[0], './../data.txt'), 'r')
lines = [l.rstrip() for l in f.readlines()]

def isVisible(tree, r, c):
    #visible from top
    maxTop=0
    for rt in range(r):
        if int(lines[rt][c]) > maxTop:
            maxTop = int(lines[rt][c])
    if maxTop < tree:
        return True
    
    #visible from right
    maxRight=0
    for cr in range(c+1, len(lines[r])):
        if int(lines[r][cr]) > maxRight:
            maxRight = int(lines[r][cr])
    if maxRight < tree:
        return True
    
    #visible from bottom
    maxBottom=0
    for rb in range(r+1, len(lines)):
        if int(lines[rb][c]) > maxBottom:
            maxBottom = int(lines[rb][c])
    if maxBottom < tree:
        return True
    
    #visible from bottom
    maxLeft=0
    for cl in range(c):
        if int(lines[r][cl]) > maxLeft:
            maxLeft = int(lines[r][cl])
    if maxLeft < tree:
        return True
    
    return False


visibleTrees = 0
for r in range(1, len(lines)-1):
    for c in range(1, len(lines[r])-1):
        tree = int(lines[r][c])
        if isVisible(tree, r, c):
            visibleTrees += 1

treesOnEdges = len(lines)*2 + len(lines[0])*2 - 4
print(visibleTrees + treesOnEdges)        