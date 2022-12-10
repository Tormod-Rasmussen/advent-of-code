lines = open("10/input.txt").read().splitlines()
x = 1
cycles = 1
onHold = [0, 0]
signalStrength = 0

def cycle(hold):
    global x
    global cycles
    global onHold
    global signalStrength
    global crtLine
    x, onHold[0], onHold[1] = x + onHold[0], onHold[1], hold
    if cycles == 20 or cycles == 60 or cycles == 100 or cycles == 140 or cycles == 180 or cycles == 220:
        signalStrength += x * cycles
    cycles += 1
    
for line in lines:
    if line == "noop":
        cycle(0)
        continue
    line = line.split(" ")
    cycle(int(line[1]))
    cycle(0)
print("part 1:", signalStrength)
