#--- Day 13: A Maze of Twisty Little Cubicles ---

with open('2016/13/input.txt') as f:
    fav_num = int(f.read())

def is_wall(x, y):
    return bin(x*x + 3*x + 2*x*y + y + y*y + fav_num).count('1') % 2 == 1

def get_neighbors(x, y):
    neighbors = [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]
    # remove negative coordinates
    neighbors = [(x, y) for x, y in neighbors if x >= 0 and y >= 0]
    return neighbors

def bfs(start, end=None, max_steps=None):
    queue = [(start, 0)]
    visited = set()
    while queue:
        node, steps = queue.pop(0)
        if end and node == end:
            return steps
        if max_steps and steps > max_steps:
            continue
        visited.add(node)
        for neighbor in get_neighbors(*node):
            if neighbor not in visited and not is_wall(*neighbor):
                queue.append((neighbor, steps + 1))
    return len(visited)

print('part 1:',bfs((1, 1), end=(31, 39)))
print('part 2:',bfs((1, 1), max_steps=50))
