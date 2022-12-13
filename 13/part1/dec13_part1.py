import sys
import os
import ast
f = open(os.path.join(sys.path[0], './../data.txt'), 'r')
lines = [l.rstrip() for l in f.readlines()]

def compareList(listLeft, listRight, log):
    if len(listLeft)==0 and len(listRight)!=0: #left run out of elements before right
        return True
    if len(listLeft)!=0 and len(listRight)==0: #right run out of elements before left
        return False
    if len(listLeft)==0 and len(listRight)==0: #both are empty
        return None
    if type(listLeft[0])==list or type(listRight[0])==list:
        result = compareElements(listLeft[0], listRight[0], log)
        if result == None:
            return compareElements(listLeft[1:], listRight[1:], log)
        return result
    if listLeft[0] < listRight[0]: #left is smaller than right
        return True
    if listLeft[0] > listRight[0]:#left is greater than right
        return False
    return compareElements(listLeft[1:], listRight[1:], log)

def compareElements(left, right, log=False):
    if log:
        print("Compare : {} and {}".format(left, right))
    if type(left)==list and type(right)==list:
        return compareList(left, right, log)
    if type(left)==list and type(right)==int:
        return compareList(left, [right], log)
    if type(left)==int and type(right)==list:
        return compareList([left], right, log)
    return compareList([left], [right], log)


log= True
rightOrderIndexSum = 0
packetIndex = 1
i=0
while i < len(lines):
    left, right = ast.literal_eval(lines[i]), ast.literal_eval(lines[i+1])
    if compareElements(left, right, log):
        rightOrderIndexSum += packetIndex
    if log:
        print('-------------------------')
    packetIndex +=1
    i+=3
print(rightOrderIndexSum)