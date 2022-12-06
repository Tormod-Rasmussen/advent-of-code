lines = open("4/input.txt").read().splitlines()
total = 0
for pair in lines:
    first, second = pair.split(",")
    first = first.split("-")
    second = second.split("-")
    if int(first[0]) <= int(second[0]) and int(first[1]) >= int(second[1]):
        total += 1
    elif int(second[0]) <= int(first[0]) and int(second[1]) >= int(first[1]):
        total += 1
print("part 1:", total)
total = 0
for pair in lines:
    first, second = pair.split(",")
    first = first.split("-")
    second = second.split("-")
    if int(first[0]) <= int(second[0]) and int(first[1]) >= int(second[0]):
        total += 1
    elif int(second[0]) <= int(first[0]) and int(second[1]) >= int(first[0]):
        total += 1
print("part 2:", total)
