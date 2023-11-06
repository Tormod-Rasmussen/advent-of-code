#--- Day 10: Elves Look, Elves Say ---
from itertools import groupby

with open('2015/10/input.txt') as f:
    line = f.readline()

def look_and_say(sequence, iterations):
    for _ in range(iterations):
        sequence = ''.join([str(len(list(g))) + str(k) for k, g in groupby(sequence)])
    return sequence

p1 = look_and_say(line,40)
print('part 1:',len(p1))
print('part 2:',len(look_and_say(p1,10)))
