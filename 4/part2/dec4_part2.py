import sys
import os
f = open(os.path.join(sys.path[0], './../data.txt'), 'r')
lines = [l.rstrip() for l in f.readlines()]

cpt=0

for l in lines:
    x1, x2 = [int(v) for v in l.split(',')[0].rstrip().split('-')]
    y1, y2 = [int(v) for v in l.split(',')[1].rstrip().split('-')]

    if (x1>=y1 and x2<=y2) or (y1>=x1 and y2<=x2): # fully overlap
        cpt+=1
    elif (x1>=y1 and x1<=y2) or (x2>=y1 and x2<=y2): # x overlap y
        cpt+=1
    elif(y1>=x1 and y1<=x2) or (y2>=x1 and y2<=x2): # y overlpa x
        cpt+=1

print(cpt)