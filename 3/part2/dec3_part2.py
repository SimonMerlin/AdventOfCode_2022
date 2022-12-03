import sys
import os
f = open(os.path.join(sys.path[0], './../data.txt'), 'r')
lines = [l.rstrip() for l in f.readlines()]

ALPHA = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

badgesSum = 0
i=0
while i<len(lines):
    group = lines[i:i+3]
    s1, s2, s3 = set(group[0]), set(group[1]), set(group[2])
    for k in s1&s2&s3:
        if k.isupper():
            badgesSum += ALPHA.index(k)+27
        else:
            badgesSum += ALPHA.index(k.upper())+1
    i+=3
    
print(badgesSum)