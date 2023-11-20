#--- Day 24: It Hangs in the Balance ---
from itertools import combinations
from functools import reduce

with open('2015/24/input.txt') as f:
    nums = [int(num) for num in f.read().splitlines()]

def quantum_entanglement(compartments):
    target = sum(nums)//compartments
    for i in range(1, len(nums)):
        for combo in combinations(nums, i):
            if sum(combo) == target:
                return reduce(lambda x, y: x*y, combo)

print('part 1:',quantum_entanglement(3))
print('part 2:',quantum_entanglement(4))
