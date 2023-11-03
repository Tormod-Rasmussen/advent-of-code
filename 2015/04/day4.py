#--- Day 4: The Ideal Stocking Stuffer ---
import hashlib

with open("2015/04/input.txt") as f:
    string = f.readline()
number = 0
while True:
    i = string + str(number)
    result = hashlib.md5(i.encode()).hexdigest()
    if result[:5] == "00000":
        print("part 1:",number)
        break
    number += 1

while True:
    i = string + str(number)
    result = hashlib.md5(i.encode()).hexdigest()
    if result[:6] == "000000":
        print("part 2:",number)
        break
    number += 1
