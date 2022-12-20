from math import prod
lines = open("08/input.txt").read().splitlines()
# format the input so each row of trees is a list of ints
trees = []
for row in range(len(lines)):
    trees.append([])
    for tree in range(len(lines[row])):
        trees[row].append(int(lines[row][tree]))
visible = 0 # trees visible from outside
for row in range(len(trees)):
    for num in range(len(trees[row])):
        # all trees in the 4 directions of the current tree
        left = trees[row][:num]
        right = trees[row][num+1:]
        up = [] + [tree[num] for tree in trees[:row]]
        down = [] + [tree[num] for tree in trees[row+1:]]
        # if there are 0 trees in any direction, the current tree is visible
        if len(left) == 0 or len(right) == 0 or len(up) == 0 or len(down) == 0:
            visible += 1
            continue
        # checks if the current tree is taller than all the trees in any of the directions
        if trees[row][num] > max(left):
            visible += 1
            continue
        elif trees[row][num] > max(right):
            visible += 1
            continue
        elif trees[row][num] > max(up):
            visible += 1
            continue
        elif trees[row][num] > max(down):
            visible += 1
            continue
print("part 1:", visible)

scenicScore = 0
for row in range(len(trees)):
    for num in range(len(trees[row])):
        # all trees in the 4 directions of the current tree
        left = trees[row][:num]
        right = trees[row][num+1:]
        up = [] + [tree[num] for tree in trees[:row]]
        down = [] + [tree[num] for tree in trees[row+1:]]
        # if 0 trees are visible in a direction, the score is 0
        if len(left) == 0 or len(right) == 0 or len(up) == 0 or len(down) == 0:
            continue
        visibleDirection = [0,0,0,0] # left right up down
        for i in left[::-1]:
            if i == -1:
                continue
            if i >= trees[row][num]:
                visibleDirection[0] += 1
                break
            else:
                visibleDirection[0] += 1
        for i in right:
            if i == -1:
                continue
            if i >= trees[row][num]:
                visibleDirection[1] += 1
                break
            else:
                visibleDirection[1] += 1
        for i in up[::-1]:
            if i == -1:
                continue
            if i >= trees[row][num]:
                visibleDirection[2] += 1
                break
            else:
                visibleDirection[2] += 1
        for i in down:
            if i == -1:
                continue
            if i >= trees[row][num]:
                visibleDirection[3] += 1
                break
            else:
                visibleDirection[3] += 1
        # sets the best score to the best score so far
        scenicScore = max(scenicScore, prod(visibleDirection))
print("part 2:", scenicScore)