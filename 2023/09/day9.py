#--- Day 9: Mirage Maintenance ---

with open('2023/09/input.txt') as f:
    values = [[int(i) for i in line.split()] for line in f.read().split('\n')]

part1 = 0
part2 = 0
for val in values:
    lst = [val]
    while any(i != 0 for i in lst[-1]):
        lst.append([lst[-1][i+1] - lst[-1][i] for i in range(len(lst[-1])-1)])
    lst[-1] = [0]
    for i in range(len(lst)-2,-1,-1):
        lst[i] = [
            lst[i][0]-lst[i+1][0],
            *lst[i],
            (lst[i][-1]+lst[i+1][-1])
            ]
    part1 += lst[0][-1]
    part2 += lst[0][0]

print('part 1:',part1)
print('part 2:',part2)
