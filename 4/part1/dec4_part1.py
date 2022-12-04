import sys
import os
f = open(os.path.join(sys.path[0], './../data.txt'), 'r')
lines = [l.rstrip() for l in f.readlines()]

cpt=0

for l in lines:
    x1, x2 = [int(v) for v in l.split(',')[0].rstrip().split('-')]
    y1, y2 = [int(v) for v in l.split(',')[1].rstrip().split('-')]

    if (x1>=y1 and x2<=y2) or (y1>=x1 and y2<=x2): #x inside y OR y inside x
        cpt+=1

print(cpt)