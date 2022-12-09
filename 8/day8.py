rawInput = open("8/input.txt").read().splitlines()

# formats the input so each row of trees is a list of ints
trees = []
for row in range(len(rawInput)):
    trees.append([])
    for tree in range(len(rawInput[row])):
        trees[row].append(int(rawInput[row][tree]))

visible = 0
# iterates through the trees
for row in range(len(trees)):
    for num in range(len(trees[row])):
        # makes lists of the trees around the current tree
        left = trees[row][:num]
        right = trees[row][num+1:]
        up = [] + [tree[num] for tree in trees[:row]]
        down = [] + [tree[num] for tree in trees[row+1:]]
        # if there are 0 trees in a direction, the current tree is visible
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
# iterates through the trees
for row in range(len(trees)):
    for num in range(len(trees[row])):
        # makes lists of the trees around the current tree
        left = trees[row][:num]
        right = trees[row][num+1:]
        up = [] + [tree[num] for tree in trees[:row]]
        down = [] + [tree[num] for tree in trees[row+1:]]
        # if 0 trees are visible in a direction, the score is 0
        if len(left) == 0 or len(right) == 0 or len(up) == 0 or len(down) == 0:
            continue
        # count how many trees are visible in each direction
        visibleLeft = 0
        visibleRight = 0
        visibleUp = 0
        visibleDown = 0
        for i in left[::-1]:
            if i == -1:
                continue
            if i >= trees[row][num]:
                visibleLeft += 1
                break
            else:
                visibleLeft += 1
        for i in right:
            if i == -1:
                continue
            if i >= trees[row][num]:
                visibleRight += 1
                break
            else:
                visibleRight += 1
        for i in up[::-1]:
            if i == -1:
                continue
            if i >= trees[row][num]:
                visibleUp += 1
                break
            else:
                visibleUp += 1
        for i in down:
            if i == -1:
                continue
            if i >= trees[row][num]:
                visibleDown += 1
                break
            else:
                visibleDown += 1
        # sets the best score to the best score so far
        scenicScore = max(scenicScore,(visibleLeft*visibleRight*visibleUp*visibleDown))
print("part 2:", scenicScore)