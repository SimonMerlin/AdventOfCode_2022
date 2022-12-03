import sys
import os
f = open(os.path.join(sys.path[0], './../data.txt'), 'r')
lines = [l.rstrip() for l in f.readlines()]

ALPHA = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

prioritiesSum = 0
for l in lines:
    s1, s2 = set(l[:len(l)//2]), set(l[len(l)//2:])
    for k in s1&s2:
        if k.isupper():
            prioritiesSum += ALPHA.index(k)+27
        else:
            prioritiesSum += ALPHA.index(k.upper())+1
print(prioritiesSum)

    