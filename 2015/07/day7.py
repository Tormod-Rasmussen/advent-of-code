#--- Day 7: Some Assembly Required ---

from functools import cache
with open('2015/07/input.txt') as f:
    lines = f.read().splitlines()

def get_lines():
    wires = {}
    for line in lines:
        line = line.split(' -> ')
        wires[line[1]] = line[0].split(' ')
    return wires

@cache
def get_signal(wire):
    try:
        val = int(wire)
        return val
    except:
        pass

    try:
        val = int(wires[wire])
        return val
    except:
        pass

    instruction = wires[wire]
    if 'NOT' in instruction:
        return 65535 - get_signal(instruction[1])
    elif 'AND' in instruction:
        return get_signal(instruction[0]) & get_signal(instruction[2])
    elif 'OR' in instruction:
        return get_signal(instruction[0]) | get_signal(instruction[2])
    elif 'LSHIFT' in instruction:
        return get_signal(instruction[0]) << int(instruction[2])
    elif 'RSHIFT' in instruction:
        return get_signal(instruction[0]) >> int(instruction[2])
    else:
        return get_signal(instruction[0])

wires = get_lines()
wire_a = get_signal('a')
print('Part 1:',wire_a)

wires = get_lines()
wires['b'] = [str(wire_a)]
get_signal.cache_clear()
print('Part 2:',get_signal('a'))
