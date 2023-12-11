#--- Day 3: Gear Ratios ---

with open('2023/03/input.txt') as f:
    lines = f.read().splitlines()
# add border of '.' around the grid
lines = ['.'*len(lines[0])]+lines+['.'*len(lines[0])]
for i in range(len(lines)):
    lines[i] = '.'+lines[i]+'.'

def find_adjecent(x, len_x, y):
    # finds the symbol and coordinate of adjacent gear
    stuff = '1234567890.'
    for x in range(x-len_x,x+1):
        if lines[y-1][x] not in stuff:
            return lines[y-1][x],(y-1,x)
        if lines[y][x] not in stuff:
            return lines[y][x],(y,x)
        if lines[y+1][x] not in stuff:
            return lines[y+1][x],(y+1,x)
    return False,None

part1 = 0
part2 = 0
gears = {}
for y,line in enumerate(lines):
    number = '0'
    for x, i in enumerate(line):
        if i in '1234567890':
            number += i
            continue
        elif number == '0':
            continue
        part,part_coor = find_adjecent(x,len(number),y)
        if part:
            part1 += int(number)
        # assumes gear cannot have 3 numbers next to it
        if part == '*' and part_coor in gears:
            part2 += int(number)*gears[part_coor]
        elif part == '*':
            gears[part_coor] = int(number)
        number = '0'

print('part 1:',part1)
print('part 2:',part2)
