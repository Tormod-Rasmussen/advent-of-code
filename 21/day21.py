lines = open("21/input.txt").read().splitlines()
monkeys = {}

def importData():
    for line in lines:
        line = line.split(" ")
        if len(line) == 2: # if only 2 items, it's a number
            monkeys[line[0].strip(":")] = int(line[1])
        else: # otherwise it's an expression
            monkeys[line[0].strip(":")] = line[1:4]

def calc(monkey):
    if isinstance(monkeys[monkey], (int,float)): # if it's a number, return it
        return monkeys[monkey]
    if monkeys[monkey][1] == "+": # if it's an equation, calculate it
        monkeys[monkey] = calc(monkeys[monkey][0]) + calc(monkeys[monkey][2])
    elif monkeys[monkey][1] == "*":
        monkeys[monkey] = calc(monkeys[monkey][0]) * calc(monkeys[monkey][2])
    elif monkeys[monkey][1] == "-":
        monkeys[monkey] = calc(monkeys[monkey][0]) - calc(monkeys[monkey][2])
    elif monkeys[monkey][1] == "/":
        monkeys[monkey] = calc(monkeys[monkey][0]) / calc(monkeys[monkey][2])
    elif monkeys[monkey][1] == "=": # for part 2, check if the result is correct
        if calc(monkeys[monkey][0]) == calc(monkeys[monkey][2]):
            return monkeys["humn"]
        elif calc(monkeys[monkey][0]) > calc(monkeys[monkey][2]):
            return "too low"
        else:
            return "too high"
    return monkeys[monkey]

importData()
for monkey in monkeys:
    calc(monkey)
print("part 1:",int(monkeys["root"]))

low = 1 # number is not lower than this
num = 2
high = 9999999999999 # number is not higher than this
while True:
    importData() # reset monkeys
    monkeys["humn"] = num # try a new number
    monkeys["root"][1] = "="
    result = calc("root") # check result
    # works with my input, but not with test input
    # because i only check if the right number is lower than the left. 
    # if the left is lower from the start, it tries decreasing the number from 1 to 1 indefinitely
    if result == "too low":
        low = num # number not lower than this
        num = min(num * 2, high) # new number to try
    elif result == "too high":
        high = num # number not higher than this
        num = (low + num) // 2 # new number to try
    else: # if result is correct, break loop
        break 
print("part 2:",monkeys["humn"])
