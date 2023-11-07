#--- Day 7: Recursive Circus ---
from collections import Counter
from re import sub

with open('2017/07/input.txt') as f:
    # lines = f.read().splitlines()
    line = sub(
        r'\(\d+\)', 
        '', 
        f.read().replace('\n', ' ').replace('->', '').replace(',','')
        )
list = line.split()
counts = Counter(list)
for item, count in counts.items():
    if count == 1:
        print('part 1:', item)
        break
