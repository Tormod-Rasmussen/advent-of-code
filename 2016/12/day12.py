#--- Day 12: Leonardo's Monorail ---

with open('2016/12/input.txt') as f:
    lines = f.read().splitlines()

def instructions(values):
    i=0
    while i < len(lines):
        line = lines[i].split()
        if line[0] == 'cpy':
            values[line[2]] = values[line[1]] if line[1] in values else int(line[1])
            i+=1
        elif line[0] == 'inc':
            values[line[1]]+=1
            i+=1
        elif line[0] == 'dec':
            values[line[1]]-=1
            i+=1
        elif line[1] in values and values[line[1]] != 0 or line[1] not in values and line[2] != 0:
                i+=int(line[2])
        else:
            i+= 1
    return values['a']

print('part 1:',instructions({'a':0,'b':0,'c':0,'d':0}))
print('part 2:',instructions({'a':0,'b':0,'c':1,'d':0}))
