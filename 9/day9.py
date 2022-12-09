lines = open("9/input.txt").read().splitlines()
rope = {
    0: [0, 0],  # rope head
    1: [0, 0],  # part 1 tail
    2: [0, 0],
    3: [0, 0],
    4: [0, 0],
    5: [0, 0],
    6: [0, 0],
    7: [0, 0],
    8: [0, 0],
    9: [0, 0]  # part 2 tail
}
visited = set()

# moves the head of the rope


def moveHead(head):
    if move[0] == "L":
        return [head[0] - 1, head[1]]
    elif move[0] == "R":
        return [head[0] + 1, head[1]]
    elif move[0] == "U":
        return [head[0], head[1] + 1]
    elif move[0] == "D":
        return [head[0], head[1] - 1]
    else:
        return head

# moves the tail of the rope


def moveTail(head, tail):
    # moving diagonally, only needed for part 2
    if head[0] - tail[0] == 2 and head[1] - tail[1] == 2:
        return [head[0] - 1, head[1] - 1]
    elif head[0] - tail[0] == -2 and head[1] - tail[1] == -2:
        return [head[0] + 1, head[1] + 1]
    elif head[0] - tail[0] == 2 and head[1] - tail[1] == -2:
        return [head[0] - 1, head[1] + 1]
    elif head[0] - tail[0] == -2 and head[1] - tail[1] == 2:
        return [head[0] + 1, head[1] - 1]
    # move the tail in the direction of the head
    elif head[0] - tail[0] == 2:
        return [head[0] - 1, head[1]]
    elif head[0] - tail[0] == -2:
        return [head[0] + 1, head[1]]
    elif head[1] - tail[1] == 2:
        return [head[0], head[1] - 1]
    elif head[1] - tail[1] == -2:
        return [head[0], head[1] + 1]
    else:
        return tail


for move in lines:
    move = move.split(" ")
    for i in range(int(move[1])):
        rope[0] = moveHead(rope[0])
        rope[1] = moveTail(rope[0], rope[1])
        visited.add(tuple(rope[1]))
print("part 1:", len(visited))

rope[0] = [0, 0]
rope[1] = [0, 0]
visited = set()
for move in lines:
    move = move.split(" ")
    for i in range(int(move[1])):
        rope[0] = moveHead(rope[0])
        for i in range(1, 10):
            rope[i] = moveTail(rope[i-1], rope[i])
        visited.add(tuple(rope[9]))
print("part 2:", len(visited))
