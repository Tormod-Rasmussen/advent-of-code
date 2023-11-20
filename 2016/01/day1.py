#--- Day 1: No Time for a Taxicab ---

with open('2016/01/input.txt') as f:
    instructions = [(i[0], int(i[1:])) for i in f.readline().replace(' ','').split(',')]

def find_shortest_path(instructions, part2=False):
    directions = {0: (1, 0), 1: (0, 1), 2: (-1, 0), 3: (0, -1)} # N,E,S,W
    visited = [(0,0)]
    x,y,facing = 0,0,0
    for turn,steps in instructions:
        facing = (facing + (1 if turn == 'R' else -1)) % 4
        for step in range(steps):
            x += directions[facing][0]
            y += directions[facing][1]
            if part2 and (x,y) in visited:
                return((abs(x) + abs(y)))
            visited.append((x,y))
    return (abs(x) + abs(y))

print('part 1:', find_shortest_path(instructions))

print('part 2:', find_shortest_path(instructions, True))
