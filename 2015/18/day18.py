#--- Day 18: Like a GIF For Your Yard ---
from copy import deepcopy

with open('2015/18/input.txt') as file:
    # makes a set of tuples with x,y coordinates for the lit lights
    lights = {(x, y) for y, line in enumerate(file) for x, char in enumerate(line.strip()) if char == '#'}

lights_p2 = deepcopy(lights)

def count_lit_neighbors(x, y, lights):
    # returns an int of how many neighbouring lights are lit
    return sum((i, j) in lights for i in range(x - 1, x + 2)
               for j in range(y - 1, y + 2) if (i, j) != (x, y))

def update_lights(current_lights, part2=False):
    # updates the lights with the next iteration following conway's game of life
    new_lights = { (0,0), (0,99), (99,0), (99,99) } if part2 else set()
    for x in range(100):
        for y in range(100):
            # check if light should be lit in the next iteration
            if (x, y) in current_lights and 2 <= count_lit_neighbors(x, y, current_lights) <= 3 or \
                    (x, y) not in current_lights and count_lit_neighbors(x, y, current_lights) == 3:
                new_lights.add((x, y))
    return new_lights

for i in range(100):
    lights = update_lights(lights)

print('part 1:',len(lights))

for i in range(100):
    lights_p2 = update_lights(lights_p2,part2=True)

print('part 2:', len(lights_p2))
