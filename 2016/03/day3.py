#--- Day 3: Squares With Three Sides ---

with open('2016/03/input.txt') as f:
    lines = f.read().splitlines()
numbers = [[int(x) for x in line.split()] for line in lines]

count = 0
for a, b, c in numbers:
    if a + b > c and a + c > b and b + c > a:
        count += 1
print('part 1:',count)

count = 0
for i in range(0,len(numbers),3):
    for j in range(3):
        a, b, c = numbers[i][j],numbers[i+1][j],numbers[i+2][j]
        if a + b > c and a + c > b and b + c > a:
            count += 1
print('part 2:',count)
