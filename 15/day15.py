def manhattanDistance(A,B): # distance between two points
    return sum(abs(a-b) for a,b in zip(A,B))

lines = open("15/input.txt").read().splitlines()
sensors = {} # key: sensor coordinates, value: manhattan distance to nearest beacon
for line in lines:
    line = line.split(" ")
    sensorX, sensorY = int(line[2].strip("x=,")), int(line[3].strip("y=:"))
    beaconX, beaconY = int(line[8].strip("x=,")), int(line[9].strip("y="))
    sensors[(sensorX,sensorY)] = manhattanDistance((sensorX,sensorY),(beaconX,beaconY))

def findCoordinates(sensor): # find all x coordinates in range of a sensor
    y = 2000000 # 10 for test input, 2000000 for part 1
    if sensor[1] > y:
        over = sensors[sensor] - sensor[1] + y
    elif sensor[1] < y:
        over = sensors[sensor] + sensor[1] - y
    for i in range(sensor[0]-over,sensor[0]+over):
        seen[i] = 1

seen = {} # tracks all x coordinates with a sensor within range
for sensor in sensors:
    findCoordinates(sensor)
print("part 1:",len(seen))