#--- Day 22: Wizard Simulator 20XX ---

with open('2015/22/input.txt') as f:
    lines = f.read().splitlines()

spells = {
    #name: [ cost, damage, heal, shield_dur, poison_dur, recharge_dur ]
    'Magic Missile':[53,4,0,0,0,0],
    'Drain': [73,2,2,0,0,0],
    'Shield': [113,0,0,6,0,0],
    'Poison': [173,0,0,0,6,0],
    'Recharge': [229,0,0,0,0,5],
}

def apply_effects(shield,poison,recharge,mana,boss_hp):
    # decrements the spell duration and restores mana / damages boss
    if shield:
        shield -= 1
    if poison:
        boss_hp -= 3
        poison -= 1
    if recharge:
        mana += 101
        recharge -= 1
    return shield,poison,recharge,mana,boss_hp

def simulate_fight(stats):
    '''
    fights the boss, trying every spell as long as mana_spent is less than min_mana_spent
    when a combination of spells kills the boss, sets min_mana_spent to mana_spent
    '''
    global min_mana_spent
    boss_hp = stats['boss_hp']
    boss_damage = stats['boss_damage']
    hp = stats['hp']
    mana = stats['mana']
    mana_spent = stats['mana_spent']
    shield = stats['shield']
    poison = stats['poison']
    recharge = stats['recharge']
    part2 = stats['part2']

    # player turn
    if part2:
        hp -= 1
        if hp <= 0:
            return
    if mana_spent > min_mana_spent:
        return
    
    shield,poison,recharge,mana,boss_hp = apply_effects(shield,poison,recharge,mana,boss_hp)
    # boss defeated
    if boss_hp <= 0:
        min_mana_spent = min(mana_spent, min_mana_spent)
        return

    # try every spell
    for spell in spells.values():
        if mana - spell[0] < 0:
            continue # can't afford
        if spell[3] and shield or spell[4] and poison or spell[5] and recharge:
            continue # effect already active

        # stat changes from spell cast
        new_mana = mana - spell[0]
        new_mana_spent = mana_spent + spell[0]
        new_boss_hp = boss_hp - spell[1]
        new_hp = hp + spell[2]
        new_shield = shield + spell[3]
        new_poison = poison + spell[4]
        new_recharge = recharge + spell[5]

        # boss turn
        new_shield,new_poison,new_recharge,new_mana,new_boss_hp = apply_effects(new_shield,new_poison,new_recharge,new_mana,new_boss_hp)
        if new_boss_hp <= 0:
            min_mana_spent = min(new_mana_spent, min_mana_spent)
            return

        # boss attack
        new_hp -= boss_damage if not new_shield else max(1, boss_damage - 7)

        # if not dead, go to next turn
        if new_hp > 0:
            simulate_fight(
                {'boss_hp': new_boss_hp,
                'boss_damage': boss_damage,
                'hp': new_hp,
                'mana': new_mana,
                'mana_spent': new_mana_spent,
                'shield': new_shield,
                'poison': new_poison,
                'recharge': new_recharge,
                'part2': part2
                })
    return

min_mana_spent = 100000000
simulate_fight({
    'boss_hp': int(lines[0].split()[-1]),
    'boss_damage': int(lines[1].split()[-1]),
    'hp': 50,
    'mana': 500,
    'mana_spent': 0,
    'shield': 0,
    'poison': 0,
    'recharge': 0,
    'part2': False
})
print('part 1:',min_mana_spent)

min_mana_spent = 100000000
simulate_fight({
    'boss_hp': int(lines[0].split()[-1]),
    'boss_damage': int(lines[1].split()[-1]),
    'hp': 50,
    'mana': 500,
    'mana_spent': 0,
    'shield': 0,
    'poison': 0,
    'recharge': 0,
    'part2': True
})
print('part 2:',min_mana_spent)
