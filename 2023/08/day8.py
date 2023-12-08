#--- Day 8: Haunted Wasteland ---
from math import lcm

with open('2023/08/input.txt') as f:
    instructions,lines = f.read().split('\n\n')
lines = lines.replace('(','').replace(')','').replace(',','').replace('=','').split('\n')
maps = {}
for line in lines:
    line = line.split()
    maps[line[0]] = (line[1],line[2])

def steps_to_end(loc,part2=False):
    steps = 0
    while loc[2] != 'Z' if part2 else loc != 'ZZZ':
        for i in instructions:
            loc = maps[loc][0] if i == 'L' else maps[loc][1]
            steps += 1
    return steps
print('part 1:',steps_to_end('AAA'))

location = [i for i in maps if i[2] == 'A']
steps = []
for loc in location:
    steps.append(steps_to_end(loc,True))
print('part 2:',lcm(*steps))
