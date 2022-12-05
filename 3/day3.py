with open("3/input.txt") as f:
    total = 0
    data = f.readlines()
    data = [x.strip() for x in data]
    for line in data:
        first_half = line[:len(line)//2]
        second_half = line[len(line)//2:]
        for letter in first_half:
            if letter in second_half:
                if letter.islower():
                    total += ord(letter) - 96
                else:
                    total += ord(letter) - 38
                break
    print("part 1:", total)
    total = 0
    for first in data[0::3]:
        second = data[data.index(first) + 1]
        third = data[data.index(first) + 2]
        for letter in first:
            if letter in second and letter in third:
                if letter.islower():
                    total += ord(letter) - 96
                else:
                    total += ord(letter) - 38
                break
    print("part 2:", total)
