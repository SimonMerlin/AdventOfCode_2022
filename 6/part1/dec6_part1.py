import sys
import os
f = open(os.path.join(sys.path[0], './../data.txt'), 'r')
lines = [l.rstrip() for l in f.readlines()]

buffer = lines[0]
for i in range(4, len(buffer)):
    uniqueString = set(buffer[i-4:i])
    if len(uniqueString) == 4:
        print(i)
        break