import sys
import os
f = open(os.path.join(sys.path[0], './../data.txt'), 'r')
lines = [l.rstrip() for l in f.readlines()]

cycle = 0
xValue=1

CRT = [[], [], [], [], [], [], []]

def drawPixel():
    global cycle, CRT, xValue
    row = cycle // 40
    index = cycle % 40 
    if index in [xValue-1, xValue, xValue+1]:
        CRT[row] += '#'
    else:
        CRT[row] += '.'


def processAddx(value):
    global cycle, xValue
    for i in range(2):
        #start cycle
        drawPixel()
        cycle += 1
        #end cycle
        if i==1:
            xValue += value

def processNoop():
    global cycle, xValue
    #start cycle
    drawPixel()
    cycle += 1
    #end cycle


for l in lines:
    l = l.split()
    if len(l) == 1: #noop
        processNoop()
    else: #addx
        processAddx(int(l[1]))


for l in CRT:
    print(''.join(l))