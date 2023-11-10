#--- Day 17: No Such Thing as Too Much ---
from itertools import combinations

with open('2015/17/input.txt') as f:
    lines = f.read().splitlines()
lines = [int(i) for i in lines]
litres = 150
total = 0
smallest_num_containers = len(lines)
for i in range(len(lines)):
    for combo in combinations(lines,i):
        if sum(combo) == litres:
            smallest_num_containers = min(smallest_num_containers,len(combo))
            total += 1
print('part 1:',total)

total = 0
for i in range(len(lines)):
    for combo in combinations(lines,i):
        if sum(combo) == litres and len(combo) == smallest_num_containers:
            total += 1
print('part 2:',total)
