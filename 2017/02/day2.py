#--- Day 2: Corruption Checksum ---
from itertools import permutations

with open('2017/02/input.txt') as f:
    lines = f.read().splitlines()

checksum = 0
for line in lines:
    line = line.split()
    biggest, smallest = int(line[0]), int(line[0])
    for num in line:
        smallest = min(smallest, int(num))
        biggest = max(biggest, int(num))
    checksum += biggest - smallest

print('part 1:',checksum)

checksum = 0
for line in lines:
    line = line.split()
    test = permutations(line,2)
    for i in test:
        if int(i[0]) % int(i[1]) == 0:
            print(int(i[0]) % int(i[1]))
            checksum += int(i[0]) // int(i[1])
            break

print('part 2:',checksum)
