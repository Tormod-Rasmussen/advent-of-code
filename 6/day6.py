input = open("6/input.txt").readlines()[0]
for i in range(len(input)):
    if len(set(input[i:i+4])) == 4:
        print("part 1:", i+4)
        break
for i in range(len(input)):
    if len(set(input[i:i+14])) == 14:
        print("part 2:", i+14)
        break