def manhattanDistance(A,B): # distance between two points
    return sum(abs(a-b) for a,b in zip(A,B))

lines = open("15/input.txt").read().splitlines()
sensors = {} # key: sensor coordinates, value: manhattan distance to nearest beacon
for line in lines:
    line = line.split(" ")
    sensorX, sensorY = int(line[2].strip("x=,")), int(line[3].strip("y=:"))
    beaconX, beaconY = int(line[8].strip("x=,")), int(line[9].strip("y="))
    sensors[(sensorX,sensorY)] = manhattanDistance((sensorX,sensorY),(beaconX,beaconY))

seen = {} # tracks all x coordinates with a sensor within range
y = 2000000 # 10 for test, 2000000 for part 1
for sensor in sensors:
    over = sensors[sensor] - sensor[1] + y if sensor[1] > y else sensors[sensor] + sensor[1] - y
    for i in range(sensor[0]-over,sensor[0]+over):
        seen[i] = 1
print("part 1:",len(seen))
