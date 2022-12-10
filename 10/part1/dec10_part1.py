import sys
import os
f = open(os.path.join(sys.path[0], './../data.txt'), 'r')
lines = [l.rstrip() for l in f.readlines()]

cycle = 0
xValue=1

signalStrengthSum = 0

def processAddx(value):
    global cycle, xValue, signalStrengthSum
    for i in range(2):
        #start cycle
        cycle += 1
        if cycle % 40 == 20:
            signalStrengthSum += cycle * xValue
        #end cycle
        if i==1:
            xValue += value

def processNoop():
    global cycle, xValue, signalStrengthSum
    #start cycle
    cycle += 1
    if cycle % 40 == 20:
        signalStrengthSum += cycle * xValue
    #end cycle


for l in lines:
    l = l.split()
    if len(l) == 1: #noop
        processNoop()
    else: #addx
        processAddx(int(l[1]))

print(signalStrengthSum)