#--- Day 4: High-Entropy Passphrases ---
from itertools import permutations

with open('2017/04/input.txt') as f:
    lines = f.read().splitlines()
valid = 0
for line in lines:
    line = line.split()
    if len(set(line)) == len(line):
        valid += 1

print('part 1:',valid)

valid = 0
for line in lines:
    words = line.split()
    sorted_words_set = set(tuple(sorted(word)) for word in words)
    if len(set(words)) == len(words) and len(sorted_words_set) == len(words):
        valid += 1

print('part 2:', valid)
