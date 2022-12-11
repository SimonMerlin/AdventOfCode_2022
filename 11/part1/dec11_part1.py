from enum import Enum
import sys
import os
import re
import math
f = open(os.path.join(sys.path[0], './../data.txt'), 'r')
lines = [l.rstrip() for l in f.readlines()]

class OP(Enum):
    MULTIPLY = "*"
    ADD = "+"
    SQUARE = "²"
    
class Item:
    def __init__(self, worryLevel):
        self.worryLevel = worryLevel
    def divideWorryLevelBy3(self):
        self.worryLevel = math.floor(self.worryLevel / 3)
    def increaseWorryLevel(self, value):
        self.worryLevel += value
    def multiplyWorryLevel(self, value):
        self.worryLevel *= value
    def squareWorryLevel(self):
        self.worryLevel *= self.worryLevel
    def __str__(self):
        return "Item: " + str(self.worryLevel)


class Monkey:
    def __init__(self, id):
        self.id = id
        self.items = []
        self.op = None
        self.opValue = None
        self.testValue = None
        self.currentItem = None
        self.monkeyTrue = None
        self.monkeyFalse = None
        self.inspectCounter = 0
    
    def setOp(self, op, value):
        self.op = op
        self.opValue = value

    def setTest(self, testValue):
        self.testValue = testValue
    
    def addItem(self, item):
        self.items.append(item)
    
    def parseThrowItem(self, line):
        monkeyId = re.findall('\d+', line)[0]
        if "true" in line:
            self.monkeyTrue = int(monkeyId)
        else:
            self.monkeyFalse = int(monkeyId)
    
    def inpectItem(self):
        self.inspectCounter += 1
        self.currentItem = self.items[0]
        self.items = self.items[1:]
        if self.op == OP.ADD:
            self.currentItem.increaseWorryLevel(self.opValue)
        elif self.op == OP.MULTIPLY:
            self.currentItem.multiplyWorryLevel(self.opValue)
        else:
            self.currentItem.squareWorryLevel()

    def getBored(self):
        self.currentItem.divideWorryLevelBy3()
        if self.currentItem.worryLevel % self.testValue == 0:
            return self.monkeyTrue
        return self.monkeyFalse
    
    def __str__(self):
        value = "Monkey " + str(self.id) + "\n"
        value += "Items : " + ", ".join([str(i.worryLevel) for i in self.items]) + "\n"
        value += "Op : " + self.op.value + " , " + str(self.opValue) + "\n"
        value += "Test divide by : " + str(self.testValue) + "\n"
        value += "True : " + str(self.monkeyTrue) + " ; False : " + str(self.monkeyFalse) + "\n"
        return value

monkeys = []

def createMonkeys():
    global monkeys
    i = 0
    while i<len(lines):
        if len(lines[i]) > 0:
            monkeyId = re.findall('\d+', lines[i])[0]
            # create monkey
            monkey = Monkey(int(monkeyId))
            i+=1
            # items worry level values
            itemsLevel = re.findall('\d+', lines[i])
            for level in itemsLevel:
                monkey.addItem(Item(int(level)))
            i+=1
            # read op
            opValue = re.findall('\d+', lines[i])
            if len(opValue) > 0:
                if OP.ADD.value in lines[i]:
                    monkey.setOp(OP.ADD, int(opValue[0]))
                else:
                    monkey.setOp(OP.MULTIPLY, int(opValue[0]))
            else:
                monkey.setOp(OP.SQUARE, None)
            i += 1
            #read test
            testValue = re.findall('\d+', lines[i])[0]
            monkey.setTest(int(testValue))
            i += 1
            # parse if
            monkey.parseThrowItem(lines[i])
            i += 1
            monkey.parseThrowItem(lines[i])
            monkeys.append(monkey)
        i+=1

def findMonkey(monkeyId):
    global monkeys
    for m in monkeys:
        if m.id == monkeyId:
            return m

createMonkeys()
for m in monkeys:
    print(m)
print('-------------------------------------------------')
for round in range(1, 21):
    print("ROUND " + str(round))
    for monkey in monkeys:
        while len(monkey.items) > 0:
            monkey.inpectItem()
            throwId = monkey.getBored()
            m = findMonkey(throwId)
            m.addItem(monkey.currentItem)
    for m in monkeys:
        print(m)
    print('-------------------------------------------------')

for m in monkeys:
    print("Monkey {} inspected items {} times.".format(m.id, m.inspectCounter))

business = [m.inspectCounter for m in monkeys]
business = sorted(business, reverse=True)
print(business[0] * business[1])