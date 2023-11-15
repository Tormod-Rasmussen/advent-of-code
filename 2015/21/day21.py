#--- Day 21: RPG Simulator 20XX ---
from itertools import product

with open('2015/21/input.txt') as f:
    lines = f.read().splitlines()

# shop not in puzzle input so i just manually input it
weapons = {
    # name: [cost, damage, armor]
    'Dagger':[8,4,0],
    'Shortsword':[10,5,0],
    'Warhammer':[25,6,0],
    'Longsword':[40,7,0],
    'Greataxe':[74,8,0]
}
armor = {
    'Leather':[13,0,1],
    'Chainmail':[31,0,2],
    'Splintmail':[53,0,3],
    'Bandedmail':[75,0,4],
    'Platemail':[102,0,5]
}
rings = {
    'Damage +1':[25,1,0],
    'Damage +2':[50,2,0],
    'Damage +3':[100,3,0],
    'Defense +1':[20,0,1],
    'Defense +2':[40,0,2],
    'Defense +3':[80,0,3]
}

def simulate_fight(armor, damage):
    # returns True if player wins
    hp = 100
    boss_hp = int(lines[0].split()[-1])
    boss_damage = int(lines[1].split()[-1])
    boss_armor = int(lines[2].split()[-1])

    while hp > 0 and boss_hp > 0:
        boss_hp -= max(damage - boss_armor,1)
        hp -= max(boss_damage - armor,1)
    # player attacks first each turn so no need to check player hp
    if boss_hp < 0:
        return True

combinations = []

# Generate all combinations of 1 weapon, 0-1 armor, and 0-2 rings
for (weapon_name, weapon_stats), (armor_name, armor_stats), \
    (ring1_name, ring1_stats), (ring2_name, ring2_stats) in product(
    weapons.items(),
    [('No Armor', [0, 0, 0])] + list(armor.items()),
    [('No Ring', [0, 0, 0])] + list(rings.items()),
    [('No Ring', [0, 0, 0])] + list(rings.items())
    ):

    # Skip combinations with duplicate rings
    if ring1_name != 'No Ring' and ring1_name == ring2_name:
        continue

    # find total cost, damage, and armor
    total_cost = sum([weapon_stats[0], armor_stats[0], ring1_stats[0], ring2_stats[0]])
    total_damage = sum([weapon_stats[1], ring1_stats[1], ring2_stats[1]])
    total_armor = sum([weapon_stats[2], armor_stats[2], ring1_stats[2], ring2_stats[2]])

    combinations.append({
        'Weapon': weapon_name,
        'Armor': armor_name,
        'Ring 1': ring1_name,
        'Ring 2': ring2_name,
        'Total Cost': total_cost,
        'Total Damage': total_damage,
        'Total Armor': total_armor
    })

# sort by cost and simulate until player wins
combinations.sort(key=lambda x: x['Total Cost'])
for combination in combinations:
    if simulate_fight(combination['Total Armor'],combination['Total Damage']):
        print('part 1:',combination['Total Cost'])
        break

# sort by reverse cost and simulate until player loses
combinations.sort(key=lambda x: x['Total Cost'], reverse=True)
for combination in combinations:
    if not simulate_fight(combination['Total Armor'],combination['Total Damage']):
        print('part 2:',combination['Total Cost'])
        break
