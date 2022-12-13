import sys
import os
import ast
from functools import cmp_to_key
f = open(os.path.join(sys.path[0], './../data.txt'), 'r')
lines = [l.rstrip() for l in f.readlines()]

def compareList(listLeft, listRight):
    if len(listLeft)==0 and len(listRight)!=0: #left run out of elements before right
        return -1
    if len(listLeft)!=0 and len(listRight)==0: #right run out of elements before left
        return 1
    if len(listLeft)==0 and len(listRight)==0: #both are empty
        return None
    if type(listLeft[0])==list or type(listRight[0])==list:
        result = compareElements(listLeft[0], listRight[0])
        if result == None:
            return compareElements(listLeft[1:], listRight[1:])
        return result
    if listLeft[0] < listRight[0]: #left is smaller than right
        return -1
    if listLeft[0] > listRight[0]:#left is greater than right
        return 1
    return compareElements(listLeft[1:], listRight[1:])

def compareElements(left, right):
    if type(left)==list and type(right)==list:
        return compareList(left, right)
    if type(left)==list and type(right)==int:
        return compareList(left, [right])
    if type(left)==int and type(right)==list:
        return compareList([left], right)
    return compareList([left], [right])

lines = [ast.literal_eval(l) for l in lines if l!=""]
packet1 = [[2]]
packet2 = [[6]]
lines.append(packet1)
lines.append(packet2)
lines.sort(key=cmp_to_key(compareElements))

print((lines.index(packet1)+1) * (lines.index(packet2)+1))