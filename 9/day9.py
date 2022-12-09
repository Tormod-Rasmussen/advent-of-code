lines = open("9/input.txt").read().splitlines()
# x, y are the coordinates of the head of the rope
x, y = 0, 0
tail = [0, 0]
visited = set()
for move in lines:
    move = move.split(" ")
    for i in range(int(move[1])):
        # move head
        if move[0] == "L":
            x -= 1
        elif move[0] == "R":
            x += 1
        elif move[0] == "U":
            y += 1
        elif move[0] == "D":
            y -= 1
        # move tail
        if x - tail[0] == 2:
            tail = [x - 1, y]
        elif x - tail[0] == -2:
            tail = [x + 1, y]
        elif y - tail[1] == 2:
            tail = [x, y - 1]
        elif y - tail[1] == -2:
            tail = [x, y + 1]
        # update visited spaces
        visited.add(tuple(tail))
print("part 1:", len(visited))
