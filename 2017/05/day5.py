#--- Day 5: A Maze of Twisty Trampolines, All Alike ---

with open('2017/05/input.txt') as f:
    lines = f.read().splitlines()

part1 = [int(i) for i in lines]
part2 = part1[:]

position = steps = 0
while position < len(part1):
    steps += 1
    command = part1[position]
    part1[position] += 1
    position += command

print('part 1:',steps)

position = steps = 0
while position < len(part2):
    steps += 1
    command = part2[position]
    if part2[position] >= 3:
        part2[position] -= 1
    else:
        part2[position] += 1
    position += command

print('part 2:',steps)
