outcomes = {
    "A X":4,
    "A Y":8,
    "A Z":3,
    "B X":1,
    "B Y":5,
    "B Z":9,
    "C X":7,
    "C Y":2,
    "C Z":6
}
score = 0
with open("2/input.txt") as f:
    score = sum(outcomes[line[:3]] for line in f)
print("part 1:",score)
outcomes = {
    "A X":3,
    "A Y":4,
    "A Z":8,
    "B X":1,
    "B Y":5,
    "B Z":9,
    "C X":2,
    "C Y":6,
    "C Z":7
}
with open("2/input.txt") as f:
    score = sum(outcomes[line[:3]] for line in f)
print("part 2:",score)
