#--- Day 11: Cosmic Expansion ---
from itertools import combinations

with open('2023/11/input.txt') as f:
    grid = f.read().splitlines()

# find x / y coordinates that have expanded
expand = 1 # num expands to make
expand_y = []
expand_x = []
for i in range(len(grid[0])):
    horiz = [grid[j][i] for j in range(len(grid))]
    if '#' not in horiz:
        expand_x.append(i)
for i in range(len(grid)):
    if '#' not in grid[i]:
        expand_y.append(i)

# find galaxy coordinates
galaxies = []
for i, row in enumerate(grid):
    for j, cell in enumerate(row):
        if cell == '#':
            galaxies.append((i, j))

def expand_spaces(x,y,lst):
    # returns number of expanding spaces are traversed
    count = 0
    x,y=min(x,y),max(x,y)
    for num in lst:
        if x < num < y:
            count += 1
    return count

def get_distances():
    pairs = combinations(galaxies,2)
    distance = 0
    for pair in pairs:
        gal1, gal2 = pair
        y_dis = abs(gal1[0]-gal2[0])
        y_dis += expand*expand_spaces(gal1[0],gal2[0],expand_y)
        x_dis = abs(gal1[1]-gal2[1])
        x_dis += expand*expand_spaces(gal1[1],gal2[1],expand_x)
        distance += y_dis+x_dis
    return distance
print('part 1:',get_distances())

expand = 999999 # add 999999 to get 1000000 spaces
print('part 2:',get_distances())
