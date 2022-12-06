import sys
import os
f = open(os.path.join(sys.path[0], './../data.txt'), 'r')
lines = [l.rstrip() for l in f.readlines()]

buffer = lines[0]
for i in range(14, len(buffer)):
    uniqueString = set(buffer[i-14:i])
    if len(uniqueString) == 14:
        print(i)
        break