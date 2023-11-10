#--- Day 14: Reindeer Olympics ---

with open('2015/14/input.txt') as f:
    lines = f.read().splitlines()

stats = {} #deer: [speed, duration, resting duration]
for line_index in range(len(lines)):
    line = lines[line_index].split()
    stats[line_index] = [int(line[3]), int(line[6]), int(line[13])]

def calculate_distance(speed,duration,rest, time):
    # returns total traveled after x time
    cycles = time // (duration + rest)
    remaining = time % (duration + rest)
    return speed * (cycles * duration + min(remaining, duration))

print('part 1:',max(calculate_distance(speed,duration,rest,2503) for speed,duration,rest in stats.values()))

points = [0]*len(lines)
for line_index in range(1,2504):
    # calculate distances traveled for each second, add a point to the ones in the lead
    distances = [calculate_distance(deer[0], deer[1], deer[2], line_index) for deer in stats.values()]
    for j in range(len(points)):
        points[j] += 1 if distances[j] == max(distances) else 0
print('part 2:',max(points))
