import sys
import os
f = open(os.path.join(sys.path[0], './../data.txt'), 'r')
lines = [l.rstrip() for l in f.readlines()]


#games values
gamesValues = {
    "X":0, #lose
    "Y":3, #draw
    "Z":6  #win
}

#shapes values
choosenShapeValue = {
    "A X":3,
    "A Y":1,
    "A Z":2,
    "B X":1,
    "B Y":2,
    "B Z":3,
    "C X":2,
    "C Y":3,
    "C Z":1
}

score = sum([choosenShapeValue[l] + gamesValues[l[2]] for l in lines])

print(score)