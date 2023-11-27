#--- Day 7: Internet Protocol Version 7 ---
from re import findall,split

with open('2016/07/input.txt') as f:
    lines = f.read().splitlines()

def abba(st):
    for i in range(len(st)-3):
        if st[i] == st[i+3] and st[i+1] == st[i+2] and st[i] != st[i+1]:
            return True

count = 0
for line in lines:
    brackets = findall(r'\[([^\]]*)\]',line)
    if any(abba(st) for st in brackets):
        continue
    if any(abba(st) for st in split(r'\[|\]', line)):
        count += 1
print('part 1:',count)

def aba_bab(line):
    line = line.replace(']','[').split('[')
    all_super,all_hyper = line[::2],line[1::2]
    aba = set()
    # find all bab in hypernet, add the coresponding aba to the set aba
    for string in range(len(all_hyper)):
        hypernet = all_hyper[string]
        for i in range(len(hypernet) - 2):
            if hypernet[i] == hypernet[i + 2] and hypernet[i] != hypernet[i+1]:
                aba.add(str(hypernet[i+1]+hypernet[i]+hypernet[i+1]))
    if not aba:
        return 0
    # look through the supernet for any aba that matches
    for string in range(len(all_super)):
        supernet = all_super[string]
        for i in range(len(supernet) - 2):
            if supernet[i:i+3] in aba and supernet[i] != supernet[i+1]:
                return 1
    return 0

count = 0
for line in lines:
    count += aba_bab(line)

print('part 2:',count)
