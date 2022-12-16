lines = open("14/input.txt").read().splitlines()
def makeGrid():
    grid = {}
    for y in range(170):            # 170 tall
        for x in range(250,750):   # width between 250 and 750
            grid[(x, y)] = "."
    for line in lines:
        line = line.split(" -> ")
        for i in range(len(line)):
            line[i] = line[i].split(",")
            line[i] = (int(line[i][0]), int(line[i][1]))
        for i in range(len(line)-1):
            x1, y1 = line[i+1]
            x2, y2 = line[i]
            x1, x2 = min(x1, x2), max(x1, x2)
            y1, y2 = min(y1, y2), max(y1, y2)
            if x1 == x2:
                while y1 <= y2:
                    grid[(x1, y1)] = "#"
                    y1 += 1
            else:
                while x1 <= x2:
                    grid[(x1, y1)] = "#"
                    x1 += 1
    return grid

def sandFalling():
    sandAmount = 0 # amount of sand
    sandPos = (500, 0) # spawn sand at 500,0
    while sandPos[1] < 169: # while sand is in grid
        if grid[sandPos[0],sandPos[1]+1] != ".": # if it can't go down, check diagonals
            if grid[sandPos[0]-1,sandPos[1]+1] != ".": # if it can't go diagonal left
                if grid[sandPos[0]+1,sandPos[1]+1] != ".": # if it can't go diagonal right
                    if sandPos == (500,0): # if the sand entrence is blocked
                        return sandAmount+1 # including the one at 500,0
                    grid[sandPos] = "o" # place sand on grid
                    sandAmount += 1 # increment sand amount
                    sandPos = (500, 0) # spawn new sand
                else: sandPos = (sandPos[0]+1, sandPos[1]+1) # nothing diagonal right, move sand diagonal right
            else: sandPos = (sandPos[0]-1, sandPos[1]+1) # nothing diagonal left, move sand diagonal left
        else: sandPos = (sandPos[0], sandPos[1]+1) # nothing under, move sand down
    return sandAmount # return amount of sand

grid = makeGrid()
print("part 1:",sandFalling())

grid = makeGrid() # remake grid to remove sand
lowestRock = 0 # lowest rock formation (highest y value)
for y in range(169,0,-1):
    for x in range(250,750):
        if grid[(x, y)] == "#":
            lowestRock = y
            break
    if lowestRock != 0:
        break

for x in range(250,750):
    grid[(x, lowestRock+2)] = "#"# add floor to grid
print("part 2:",sandFalling())
