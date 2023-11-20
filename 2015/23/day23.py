#--- Day 23: Opening the Turing Lock ---

with open('2015/23/input.txt') as f:
    lines = f.read().splitlines()
lines = [line.replace(',','').split() for line in lines]

def find_b():
    i=0
    while i < len(lines):
        if lines[i][0] == 'hlf':
            registers[lines[i][1]] //= 2
        elif lines[i][0] == 'tpl':
            registers[lines[i][1]] *= 3
        elif lines[i][0] == 'inc':
            registers[lines[i][1]] += 1
        elif lines[i][0] == 'jmp':
            i += int(lines[i][1])-1
        elif lines[i][0] == 'jie':
            if registers[lines[i][1]] % 2 == 0:
                i += int(lines[i][2])-1
        elif lines[i][0] == 'jio':
            if registers[lines[i][1]] == 1:
                i += int(lines[i][2])-1
        i+=1

registers = {'a': 0, 'b': 0}
find_b()
print('part 1:',registers['b'])

registers = {'a': 1, 'b': 0}
find_b()
print('part 1:',registers['b'])
