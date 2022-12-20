total = 0
lines = open("03/input.txt").read().splitlines()
for line in lines:
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
for first in lines[0::3]:
    second = lines[lines.index(first) + 1]
    third = lines[lines.index(first) + 2]
    for letter in first:
        if letter in second and letter in third:
            if letter.islower():
                total += ord(letter) - 96
            else:
                total += ord(letter) - 38
            break
print("part 2:", total)