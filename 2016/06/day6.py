#--- Day 6: Signals and Noise ---
from collections import Counter

with open('2016/06/input.txt') as f:
    lines = f.read().splitlines()

message = ''.join(Counter(line[i] for line in lines).most_common(1)[0][0] for i in range(len(lines[0])))
print('part 1:',message)

message = ''.join(Counter(line[i] for line in lines).most_common()[-1][0] for i in range(len(lines[0])))
print('part 2:',message)
