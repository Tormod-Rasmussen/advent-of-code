string = open("6/input.txt").read()
for i in range(len(string)):
    if len(set(string[i:i+4])) == 4:
        print("part 1:", i+4)
        break
for i in range(len(string)):
    if len(set(string[i:i+14])) == 14:
        print("part 2:", i+14)
        break
