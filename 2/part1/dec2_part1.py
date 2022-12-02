import sys
import os
f = open(os.path.join(sys.path[0], './../data.txt'), 'r')
lines = [l.rstrip() for l in f.readlines()]


#shapes values
shapesValues = {
    "X":1,
    "Y":2,
    "Z":3
}

#games values
gamesValues = {
    "A X":3,
    "A Y":6,
    "A Z":0,
    "B X":0,
    "B Y":3,
    "B Z":6,
    "C X":6,
    "C Y":0,
    "C Z":3
}

score = sum([gamesValues[l] + shapesValues[l[2]] for l in lines])

print(score)