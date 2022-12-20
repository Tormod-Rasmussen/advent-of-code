lines = open("02/input.txt").readlines()
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
score = sum(outcomes[line[:3]] for line in lines)
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
score = sum(outcomes[line[:3]] for line in lines)
print("part 2:",score)