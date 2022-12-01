bag = []
temp = 0
with open("1/input.txt") as f:
    data = f.read().splitlines()
    data.append("")
    for line in data:
        if line != "":
            temp += int(line)
        else:
            bag.append(temp)
            temp = 0
bag.sort()
print("part 1:",bag[-1])
print("part 2:",sum(bag[-3:]))