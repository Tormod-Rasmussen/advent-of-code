#--- Day 8: Matchsticks ---

with open('2015/08/input.txt') as f:
    lines = f.read().splitlines()

count, count2 = 0,0
for line in lines:
    count += len(line) - len(eval(line))
    count2 += line.count('"') + line.count('\\') + 2

print('part 1:',count)
print('part 2:',count2)
