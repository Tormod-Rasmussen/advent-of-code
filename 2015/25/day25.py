#--- Day 25: Let It Snow ---

with open('2015/25/input.txt') as f:
    lines = f.readline().split()
row = int(lines[-3].replace(',',''))
col = int(lines[-1].replace('.',''))
num = 20151125

for _ in range((row + col - 2)*(row + col - 1)//2 + col - 1):
    num = (num * 252533) % 33554393

print('part 1:',num)
