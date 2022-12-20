bag = []
temp = 0
lines = open("01/input.txt").read().splitlines()
lines.append("")
for line in lines:
    if line != "":
        temp += int(line)
    else:
        bag.append(temp)
        temp = 0
bag.sort()
print("part 1:",bag[-1])
print("part 2:",sum(bag[-3:]))