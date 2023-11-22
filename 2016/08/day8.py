#--- Day 8: Two-Factor Authentication ---

with open('2016/08/input.txt') as f:
    lines = f.read().splitlines()

screen = [['⬛']*50 for _ in range(6)]

def rect(x_coor,y_coor):
    for y in range(y_coor):
        for x in range(x_coor):
            screen[y][x] = '⬜'

def rotate_row(coor,it):
    for _ in range(it):
        temp = screen[coor][-1]
        for i in range(len(screen[coor])-1,0,-1):
            screen[coor][i] = screen[coor][i-1]
        screen[coor][0] = temp

def rotate_column(coor,it):
    for _ in range(it):
        temp = screen[-1][coor]
        for i in range(len(screen)-1,0,-1):
            screen[i][coor] = screen[i-1][coor]
        screen[0][coor] = temp

for line in lines:
    if 'rect' in line:
        x,y = line.split()[-1].split('x')
        rect(int(x),int(y))
    elif 'row' in line:
        coor,i = line.split('=')[1].split(' by ')
        rotate_row(int(coor),int(i))
    else:
        coor,i = line.split('=')[1].split(' by ')
        rotate_column(int(coor),int(i))

count_lit = sum([line.count('⬜') for line in screen])
print('part 1:',count_lit)

print('part 2:')
for line in screen:
    print(''.join(line))
