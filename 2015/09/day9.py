#--- Day 9: All in a Single Night ---
from itertools import permutations

with open('2015/09/input.txt') as f:
    lines = f.read().splitlines()

all_times = []
paths = {}
cities = set()

for line in lines:
    line = line.split(" ")
    city_pair = frozenset({line[0], line[2]})
    paths[city_pair] = int(line[4])
    cities.update({line[0],line[2]})

for path in permutations(cities):
    time = 0
    for i in range(len(path)-1):
        city_pair = frozenset({path[i], path[i + 1]})
        time += paths[city_pair]
    all_times.append(time)
print(min(all_times))
print(max(all_times))
