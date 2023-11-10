#--- Day 17: No Such Thing as Too Much ---
from itertools import combinations

with open('2015/17/input.txt') as f:
    lines = f.read().splitlines()
lines = [int(i) for i in lines]
litres = 150
total = 0
for i in range(len(lines)):
    for combo in combinations(lines,i):
        if sum(combo) == litres:
            total += 1
print('part 1:',total)

total = 0
for i in range(len(lines)):
    for combo in combinations(lines,i):
        if sum(combo) == litres:
            total += 1
    if total != 0:
        break
print('part 2:',total)
