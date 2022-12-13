lines = open("11/input.txt").read().splitlines()
monkeys = {}
def getInput(lines):
    for i in range(0, len(lines), 7):
        monkey = int(lines[i].strip("Monkey :"))
        items = lines[i+1].strip("Starting items:").split(", ")
        items = [int(item) for item in items]
        expression = lines[i+2].split(" ")[6:]
        divisibleBy = int(lines[i + 3].strip("Test: divisible by"))
        true_result = int(lines[i + 4].strip("If true: throw to monkey"))
        false_result = int(lines[i + 5].strip("If false: throw to monkey"))
        monkeys[monkey] = [
            items,          # list of items
            expression,     # * or + and number
            divisibleBy,    # number to check
            true_result,    # monkey to throw to if True
            false_result,   # monkey to throw to if False
            0               # times the monkey has checked an item
            ]
def monkeyBussiness(worryDown,iterations):
    multi = 1 # find common multiplier
    for i in monkeys.keys():
        multi *= monkeys[i][2]
    for i in range(iterations):
        for ape in monkeys:
            ape = monkeys[ape]
            while len(ape[0]) > 0:
                if ape[1][0] == "*":
                    try:
                        ape[0][0] *= int(ape[1][1])
                    except ValueError:
                        ape[0][0] *= ape[0][0]
                else:
                    ape[0][0] += int(ape[1][1])
                if worryDown:
                    ape[0][0] //= 3
                else:
                    ape[0][0] %= multi
                if ape[0][0] % ape[2] == 0:
                    monkeys[ape[3]][0].append(ape[0][0])
                else:
                    monkeys[ape[4]][0].append(ape[0][0])
                ape[5] += 1
                ape[0].pop(0)
    return sorted([i[5] for i in monkeys.values()])
    
getInput(lines)
part1 = monkeyBussiness(True,20)
print("part 1:", part1[-1]*part1[-2])

getInput(lines)
part2 = monkeyBussiness(False,10000)
print("part 2:", part2[-1]*part2[-2])