#--- Day 2: Bathroom Security ---

with open('2016/02/input.txt') as f:
    lines = f.read().splitlines()
keypad = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
y,x = 1,1
number = ''
directions = {'U': (-1, 0), 'R': (0, 1), 'D': (1, 0), 'L': (0, -1)} # URDL
for line in lines:
    for move in line:
        y = max(min((y + directions[move][0]),2),0)
        x = max(min((x + directions[move][1]),2),0)
    number += str(keypad[y][x])

print('part 1:',number)

keypad = [
    [0,0,0,0,0,0,0],
    [0,0,0,1,0,0,0],
    [0,0,2,3,4,0,0],
    [0,5,6,7,8,9,0],
    [0,0,'A','B','C',0,0],
    [0,0,0,'D',0,0,0],
    [0,0,0,0,0,0,0]
]
number = ''
y,x = 3,1
for line in lines:
    for move in line:
        new_y = y+directions[move][0]
        new_x = x+directions[move][1]
        if keypad[new_y][new_x] != 0:
            y,x = new_y,new_x
    number += str(keypad[y][x])

print('part 2:',number)
