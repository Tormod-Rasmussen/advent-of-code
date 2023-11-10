#--- Day 15: Science for Hungry People ---
from itertools import product

with open('2015/15/input.txt') as f:
    lines = f.readlines()

ingredients = [] #[capacity, durability, flavor, texture, calories]
for line in lines:
    _, _, capacity, _, durability, _, flavor, _, texture, _, calories = line.split()
    ingredients.append([int(capacity[:-1]), int(durability[:-1]), int(flavor[:-1]), int(texture[:-1]), int(calories)])

def make_cookies(ingredients, sum_calories=0):
    best_score = 0
    for amounts in product(range(101), repeat=len(ingredients)):
        if sum(amounts) != 100:
            continue
        calories = sum(amounts[i]*ingredients[i][4] for i in range(len(ingredients)))
        if sum_calories and calories != sum_calories:
            continue
        capacity = sum(amounts[i]*ingredients[i][0] for i in range(len(ingredients)))
        durability = sum(amounts[i]*ingredients[i][1] for i in range(len(ingredients)))
        flavor = sum(amounts[i]*ingredients[i][2] for i in range(len(ingredients)))
        texture = sum(amounts[i]*ingredients[i][3] for i in range(len(ingredients)))
        score = max(0, capacity)*max(0, durability)*max(0, flavor)*max(0, texture)
        best_score = max(best_score, score)
    return best_score

print('part 1:',make_cookies(ingredients))

print('part 2:',make_cookies(ingredients,500))
