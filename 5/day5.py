import copy
input = open("5/input.txt").readlines()
part1 = ""
part2 = ""
crates = {
    "1": [],
    "2": [],
    "3": [],
    "4": [],
    "5": [],
    "6": [],
    "7": [],
    "8": [],
    "9": []
}
for line in input:
    if "[" in line:
        crates["1"].append(line[1])
        crates["2"].append(line[5])
        crates["3"].append(line[9])
        crates["4"].append(line[13])
        crates["5"].append(line[17])
        crates["6"].append(line[21])
        crates["7"].append(line[25])
        crates["8"].append(line[29])
        crates["9"].append(line[33])
        continue
    if line == "\n":
        for i in crates:
            crates[i] = [x for x in crates[i] if x != " "]
            crates[i].reverse()
            cratesPart2 = copy.deepcopy(crates)
    if "move" in line:
        line = line.rstrip()
        line = line.split(" ")
        cratesToMove = int(line[1])
        cratesPart2[line[5]] = cratesPart2[line[5]] + cratesPart2[line[3]][-cratesToMove:]
        cratesPart2[line[3]] = cratesPart2[line[3]][:-cratesToMove]
        while cratesToMove:
            crates[line[5]].append(crates[line[3]].pop())
            cratesToMove-=1
for i in crates:
    part1 += crates[i].pop()
print("part 1:",part1)
for i in cratesPart2:
    part2 += cratesPart2[i].pop()
print("part 2:",part2)
