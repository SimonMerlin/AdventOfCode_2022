import sys
import os
import re
f = open(os.path.join(sys.path[0], './../data.txt'), 'r')
lines = [l.rstrip() for l in f.readlines()]

stacks = dict()

def move(qty, _from, _to):
    crates = stacks[_from][len(stacks[_from])-qty:]
    stacks[_from] = stacks[_from][:len(stacks[_from])-qty]
    stacks[_to] = stacks[_to] + crates[::-1]

def buildStacks():
    for l in lines:
        if l == "":
            return
        l = re.sub('^\s{3}', '[x]', l)
        l = re.sub('\s{3}$', '[x]', l)
        l = re.sub('\s{4}', '[x]', l)
        l = "".join(re.findall('[xA-Z]', l))

        i=0
        while i<len(l):
            if l[i] != 'x' and str(i+1) in stacks:
                stacks[str(i+1)] = l[i] + stacks[str(i+1)]
            elif l[i] != 'x':
                stacks[str(i+1)] = l[i]
            i+=1

def process():
    process = False
    i=0
    while i<len(lines):
        l=lines[i]
        if l=="" and not process:
            process=True
        elif process:
            qty, _from, _to = re.findall('\d+', l)
            move(int(qty), _from, _to)
        i+=1

buildStacks()
process()

answer = ""
for k in sorted(stacks.keys()):
    if stacks[k] != "":
        answer += stacks[k][-1]

print(answer)