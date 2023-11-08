#--- Day 12: JSAbacusFramework.io ---
import re
import json

with open('2015/12/input.txt') as f:
    line = f.readline()

print('part 1:',sum(map(int, re.findall(r'-?\d+', line))))

def check_dict(items):
    total = 0
    if any(value == 'red' for value in items.values()):
        return total
    for value in items.values():
        if type(value) == int:
            total += value
        elif type(value) == dict:
            total += check_dict(value)
        elif type(value) == list:
            total += check_list(value)
    return total

def check_list(items):
    total = 0
    for i in items:
        if type(i) == int:
            total += i
        elif type(i) == dict:
            total += check_dict(i)
        elif type(i) == list:
            total += check_list(i)
    return total

formatted = json.loads(line)
total = check_list(formatted) if type(formatted) == list else check_dict(formatted)
print('part 2:',total)
