#--- Day 8: I Heard You Like Registers ---

with open('2017/08/input.txt') as f:
    lines = f.read().splitlines()

variables = {}
for line in lines:
    variables[line.strip().split()[0]] = 0

highest_value = 0

for line in lines:
    line = line.split()
    if eval(f'{variables[line[4]]} {line[5]} {line[6]}'):
        if line[1] == 'inc':
            variables[line[0]] += int(line[2])
        elif line[1] == 'dec':
            variables[line[0]] -= int(line[2])
        highest_value = max(highest_value,variables[line[0]])

print('part 1:',max(variables.values()))
print('part 2:',highest_value)
