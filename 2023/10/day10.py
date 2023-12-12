#--- Day 10: Pipe Maze ---

with open('2023/10/input.txt') as f:
    grid = f.read().splitlines()

# find start
for y, line in enumerate(grid):
    x = line.find('S')
    if x >= 0:
        start = (y,x)
        break

y,x = start
visited = [start]

def find_neighbors(cur):
    neighbors = [(y,x+1,'-J7'),(y,x-1,'-FL'),(y+1,x,'|JL'),(y-1,x,'|F7')]
    if cur == 'S':
        return neighbors
    valid_move = {'-':(0,1),'F':(0,2),'L':(0,3),'7':(1,2),'J':(1,3),'|':(2,3),}
    return [neighbors[valid_move[cur][0]],neighbors[valid_move[cur][1]]]

def move():
    global x,y
    cur_pipe = grid[y][x]
    neighbors = find_neighbors(cur_pipe)
    for neighbor in neighbors:
        if neighbor[:2] not in visited and grid[neighbor[0]][neighbor[1]] in neighbor[2]:
            y,x = neighbor[0],neighbor[1]
            visited.append((y,x))
            return True

while move():
    continue

print('part 1:',len(visited)//2)

# using Point in Polygon to find tiles inside
count = 0
for y,line in enumerate(grid):
    is_inside = False
    for x,i in enumerate(line):
        if (y,x) in visited and i in '|LJ':
            is_inside = not is_inside
        if is_inside and (y,x) not in visited:
            count += 1

print('part 2:',count)
