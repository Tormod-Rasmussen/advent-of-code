#--- Day 6: Probably a Fire Hazard ---

with open("2015/06/input.txt") as f:
    lines = f.read().splitlines()
grid = [[0] * 1000 for _ in range(1000)]
for line in lines:
    instruction, start_coor, _, end_coor = line.strip().rsplit(' ',3)
    from_coor = [int(coor) for coor in start_coor.split(',')]
    dest_coor = [int(coor) for coor in end_coor.split(',')]

    for x in range(from_coor[0],dest_coor[0]+1):
        for y in range(from_coor[1], dest_coor[1]+1):
            if instruction == 'turn on':
                grid[x][y] = 1
            elif instruction == 'turn off':
                if grid[x][y] == 1:
                    grid[x][y] = 0
            else:
                grid[x][y] = 1 - grid[x][y]

print('part 1:', sum(row.count(1) for row in grid))

grid = [[0] * 1000 for _ in range(1000)]
brightness = 0
for line in lines:
    instruction, start_coor, _, end_coor = line.strip().rsplit(' ',3)
    from_coor = [int(coor) for coor in start_coor.split(',')]
    dest_coor = [int(coor) for coor in end_coor.split(',')]

    for x in range(from_coor[0],dest_coor[0]+1):
        for y in range(from_coor[1], dest_coor[1]+1):
            if instruction == 'turn on':
                brightness += 1
                grid[x][y] += 1
            elif instruction == 'turn off':
                if grid[x][y] > 0:
                    brightness -= 1
                    grid[x][y] -= 1
            else:
                brightness += 2
                grid[x][y] += 2

print('part 2:', brightness)
