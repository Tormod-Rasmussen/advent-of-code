#--- Day 1: Not Quite Lisp ---

with open("2015/01/input.txt") as f:
    string = f.read()
floor = 0
for i in range(len(string)):
    if string[i] == "(":
        floor += 1
    elif string[i] == ")":
        floor -= 1
print("part 1:",floor)

floor = 0
for i in range(len(string)):
    if string[i] == "(":
        floor += 1
    elif string[i] == ")":
        floor -= 1
    if floor < 0:
        print("part 2:",i+1)
        break
