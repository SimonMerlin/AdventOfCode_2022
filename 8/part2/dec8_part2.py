import sys
import os
f = open(os.path.join(sys.path[0], './../data.txt'), 'r')
lines = [l.rstrip() for l in f.readlines()]

def scenicScore(tree, r, c):
    #visible trees on top
    visibleTop=0
    for rt in range(r-1, -1, -1):
        if int(lines[rt][c]) < tree:
            visibleTop +=1
        else:
            visibleTop +=1
            break
    
    #visible trees on right
    visibleRight=0
    for cr in range(c+1, len(lines[r])):
        if int(lines[r][cr]) < tree:
            visibleRight += 1
        else:
            visibleRight += 1
            break
    
    #visible trees on bottom
    visibleBottom=0
    for rb in range(r+1, len(lines)):
        if int(lines[rb][c]) < tree:
            visibleBottom += 1
        else:
            visibleBottom += 1
            break
    
    #visible trees on left
    visibleLeft=0
    for cl in range(c-1, -1, -1):
        if int(lines[r][cl]) < tree:
            visibleLeft +=1
        else:
            visibleLeft +=1
            break
    return visibleTop * visibleRight * visibleBottom * visibleLeft



maxScenicValue = 0
for r in range(1, len(lines)-1):
    for c in range(1, len(lines[r])-1):
        tree = int(lines[r][c])
        scenicValue = scenicScore(tree, r, c)
        if scenicValue > maxScenicValue:
            maxScenicValue = scenicValue

print(maxScenicValue)        