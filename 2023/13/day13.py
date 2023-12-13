#---Day 13: Point of Incidence ---

with open('2023/13/input.txt') as f:
    patterns = f.read().split('\n\n')

def find_reflection(p,part2=False):
    for i in range(len(p)-1):
        mirror = p[i::-1]
        rorrim = p[i+1:len(mirror)+i+1]
        mirror = mirror[:len(rorrim)]
        if part2:
            mirror = remove_smudge(mirror,rorrim)
        if rorrim == mirror:
            return (i+1)
    return 0

def remove_smudge(mirror,rorrim):
    # changes the first unequal symbol found
    for line in range(len(mirror)):
        for i in range(len(mirror[line])):
            if mirror[line][i] != rorrim[line][i]:
                mirror[line] = mirror[line][:i] + str(rorrim[line][i]) + mirror[line][i+1:]
                return mirror
    return None

def get_reflection_sum(part2=False):
    total = 0
    for grid in patterns:
        grid = grid.split('\n')
        reflection = find_reflection(grid,part2)
        if reflection:
            total += 100*reflection
        else:
            grid = [''.join(row[i] for row in grid)[::-1] for i in range(len(grid[0]))]
            total += find_reflection(grid,part2)
    return total

print('part 1:',get_reflection_sum())
print('part 2:',get_reflection_sum(True))
