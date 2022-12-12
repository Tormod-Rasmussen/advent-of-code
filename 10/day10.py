lines = open("10/input.txt").read().splitlines()
cycle = 0
x = 1
computing = 0
signalStrength = 0
num = 0
crt = [""]*6

def clock(instruction):
    global x, cycle, computing, signalStrength, num, crt
    cycle += 1
    pos = cycle - num*40
    if x <= pos <= x+2:
        crt[num] += "⬛"
    else:
        crt[num] += "⬜"
    if cycle % 40 == 0:
        num += 1
    if (cycle -20) % 40 == 0:
        signalStrength += x*cycle
    x += computing
    computing = 0
    if instruction == "noop":
        return
    instruction = instruction.split(" ")
    computing = int(instruction[1])
    # running clock again to simulate the 2 cycles it takes to add
    clock("noop")

for line in lines:
    clock(line)
print("part 1:", signalStrength)
print("part 2:")
for line in crt:
    print(line)
