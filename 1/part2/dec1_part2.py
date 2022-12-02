import sys
import os
f = open(os.path.join(sys.path[0], './../data.txt'), 'r')
lines = [l.rstrip() for l in f.readlines()]

calories = []

#compute calories for each Elf
cpt=0
for l in lines:
    if l == "":
        calories.append(cpt)
        cpt=0
    else:
        cpt += int(l)

# print the Elf carrying the most calories
calories.sort(reverse=True)
print(sum(calories[:3]))