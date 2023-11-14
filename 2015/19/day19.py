#--- Day 19: Medicine for Rudolph ---

replacements = dict()
with open('2015/19/input.txt') as f:
    lines = f.read().splitlines()

replacements = {}
# read all replacements, store them in a dict with lists
for line in lines[:-2]:
    a, b = line.split(' => ')
    if a not in replacements:
        replacements[a] = []
    replacements[a].append(b)
molecule = lines[-1]

distinct_molecules = set()

# iterate over any possible combination in the molecule
for i in range(len(molecule)):
    for j in range(i+1, len(molecule)+1):
        # make all possible replacements and store in the set
        if molecule[i:j] in replacements:
            for replacement in replacements[molecule[i:j]]:
                distinct_molecules.add(molecule[:i] + replacement + molecule[j:])

print('part 1:',len(distinct_molecules))

# reversed replacements to work backwards to get to e
replacements = {}
for line in lines[:-2]:
    a, b = line.split(' => ')
    replacements[b] = a

# try the longest substitution until we get e
# greedy solution, might not work for every possible input
steps = 0
while molecule != 'e':
    for key in sorted(replacements, key=len, reverse=True):
        if key in molecule:
            molecule = molecule.replace(key, replacements[key], 1)
            steps += 1

print('part 2:',steps)
