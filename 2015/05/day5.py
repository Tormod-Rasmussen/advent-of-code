#--- Day 5: Doesn't He Have Intern-Elves For This? ---

with open("2015/05/input.txt") as f:
    lines = f.read().splitlines()
niceStrings = 0
for line in lines:
    if any(string in line for string in ["ab","cd","pq","xy"]):
        continue
    if not any(char1 == char2 for char1, char2 in zip(line, line[1:])):
        continue
    if sum(1 for letter in line if letter in "aeiou") >= 3:
        niceStrings += 1
print("part 1:",niceStrings)

niceStrings = 0
for line in lines:
    double_pair = False
    if not any(char1 == char2 for char1, char2, in zip(line,line[2:])):
        continue
    for i in range(len(line)-1):
        for j in range(i+2,len(line)-1):
            if line[i] == line[j] and line[i+1] == line[j+1]:
                double_pair = True
        continue
    if double_pair == True:
        niceStrings += 1
print("part 2:",niceStrings)
