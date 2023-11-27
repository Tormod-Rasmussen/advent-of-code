#--- Day 9: Explosives in Cyberspace ---

with open('2016/09/input.txt') as f:
    line = f.readline().replace(' ','')

def get_uncompressed_length(line,part2=False):
    if not '(' in line:
        return len(line)
    length = len(line.split('(',1)[0])
    line = line.split('(',1)[1]
    instructions,line = line.split(')',1)
    num_chars, repeats = map(int,instructions.split('x'))
    if part2 and ')' in line[:num_chars]:
            length += repeats*get_uncompressed_length(line[:num_chars],part2)
    else:
        length+=len(line[:num_chars])*repeats
    return length + get_uncompressed_length(line[num_chars:],part2)

print('part 1:',get_uncompressed_length(line))
print('part 2:',get_uncompressed_length(line,True))
