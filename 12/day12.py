lines = open("12/input.txt").read().splitlines()

heightmap = [[] for line in lines]
for line in range(len(lines)): 
    for letter in lines[line]:
        if letter == "S": # find start and end coordinates 
            start = (line,lines[line].index(letter))
            heightmap[line].append("S")
            continue
        elif letter == "E":
            end = (line,lines[line].index(letter))
            heightmap[line].append("E")
            continue
        else: # convert letters to numbers
            heightmap[line].append(ord(letter) - 96)
heightmap[start[0]][start[1]] = 1
heightmap[end[0]][end[1]] = 26

def shortestPath():
    visited = [start] # visited coordinates
    queue = [start] # queue of coordinates to check neighbors of
    distances = {} # tracks shortest distance from start to each coordinate
    for i in range(len(heightmap)):
        for j in range(len(heightmap[0])):
            distances[(i,j)] = 999999
    distances[start] = 0
    while queue:
        current = queue.pop(0)
        if current == end:
            break # end reached
        visited.append(current)
        directions = [(0,1),(0,-1),(1,0),(-1,0)] # right left up down
        for direction in directions:
            new = (current[0] + direction[0], current[1] + direction[1])
            if new[0] < 0 or new[1] < 0 or new[0] >= len(heightmap) or new[1] >= len(heightmap[0]):
                continue # out of bounds
            if heightmap[new[0]][new[1]] <= heightmap[current[0]][current[1]] + 1: # can move to new coordinate
                if distances[new] > distances[current] + 1: # new distance is shorter
                    queue.append(new)
                    distances[new] = distances[current] + 1
    return distances[end] # shortest distance from start to end
print("part 1:",shortestPath())

shortest = 999999
for i in range(len(heightmap)):
    for j in range(len(heightmap[0])):
        if heightmap[i][j] == 1: # find all starting points
            start = (i,j)
            shortest = min(shortest,shortestPath()) # find shortest path of all starting points
print("part 2:",shortest)