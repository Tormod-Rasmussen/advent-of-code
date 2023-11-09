#--- Day 13: Knights of the Dinner Table ---
from itertools import permutations

with open('2015/13/input.txt') as f:
    lines = f.read().splitlines()

seating_options = {}
# format input
for line in lines:
    words = line.split()
    person1 = words[0]
    person2 = words[-1][:-1]
    seating_options[(person1, person2)] = int(words[3]) * (1 if words[2] == 'gain' else -1)
people = set()
for person1, person2 in seating_options:
    people.add(person1)

max_happiness = 0
best_arrangement = None
# find the best seat arrangement and the total happiness it gives
for path in permutations(people):
    happiness = sum(
        seating_options[(p1, p2)] + seating_options[(p2, p1)] for p1, p2 in zip(path, path[1:])
    ) + seating_options[(path[0], path[-1])] + seating_options[(path[-1], path[0])]


    if happiness > max_happiness:
        max_happiness = happiness
        best_arrangement = list(path)

print('part 1:',max_happiness)

# using the best seat arrangement, sit between the weakest link
best_arrangement.append(best_arrangement[0])
weakest_link = min(seating_options[(p1,p2)] + seating_options[(p2,p1)] \
                   for p1, p2 in zip(best_arrangement, best_arrangement[1:]))

print('part 2:',max_happiness-weakest_link)
