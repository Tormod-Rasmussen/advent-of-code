lines,path = open("22/input.txt").read().split("\n\n") # split into lines and path
path = path.replace("R",",R,").replace("L",",L,").split(",") # split into list of turns and steps

grid = [list(i) for i in lines.split("\n")]
maxlen = max([len(i) for i in grid])+1
for i in range(len(grid)): # padding grid with " " to avoid index errors
    grid[i] += [" "]*(maxlen-len(grid[i])) # right padding
    grid[i].insert(0," ") # left padding
grid.insert(0,[" "]*maxlen) # top padding
grid.append([" "]*maxlen) # bottom padding

i = 0 # finding starting position
while grid[1][i] != ".":
    i += 1
position = (1,i) # 1 indexed
facing = "R" # start facing right

def turn(clockwise=True): # turn clockwise or counterclockwise
    global facing
    if facing == "R":
        facing = "D" if clockwise else "U"
    elif facing == "D":
        facing = "L" if clockwise else "R"
    elif facing == "L":
        facing = "U" if clockwise else "D"
    elif facing == "U":
        facing = "R" if clockwise else "L"

def wrap(steps): # wrap around to the other side if moving off the board
    global position
    temp = 0 # steps to move to get to a valid position
    if facing in "RL": # if facing left or right
        while grid[position[0]][temp] == " ":
            temp += 1 if facing == "R" else -1
        if grid[position[0]][temp] == "#":
            return 0 # if there is a wall, stop moving
        else:
            position = (position[0],temp) if temp >= 0 else (position[0],len(grid[position[0]])+temp)
    elif facing in "UD": # if facing up or down
        while grid[temp][position[1]] == " ":
            temp += 1 if facing == "D" else -1
        if grid[temp][position[1]] == "#":
            return 0
        else:
            position = (temp,position[1]) if temp >= 0 else (len(grid)+temp,position[1])
    return steps

def move(steps): # move forward a given number of steps
    global position
    ahead = (0,1) if facing == "R" else (1,0) if facing == "D" else (0,-1) if facing == "L" else (-1,0)
    while steps > 0:
        if grid[position[0]+ahead[0]][position[1]+ahead[1]] == "#":
            return
        elif grid[position[0]+ahead[0]][position[1]+ahead[1]] == " ":
            steps = wrap(steps)
        else:
            position = (position[0]+ahead[0],position[1]+ahead[1])
        steps -= 1

for i in path: # follow the path
    if i == "R":
        turn()
    elif i == "L":
        turn(False)
    else:
        move(int(i))

facing = 0 if facing == "R" else 1 if facing == "D" else 2 if facing == "L" else 3
print("part 1:",1000*position[0] + 4*position[1] + facing)