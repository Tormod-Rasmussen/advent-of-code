#--- Day 16: Aunt Sue ---

with open('2015/16/input.txt') as f:
    lines = f.read().splitlines()

aunt = {
'children': 3,
'cats': 7,
'samoyeds': 2,
'pomeranians': 3,
'akitas': 0,
'vizslas': 0,
'goldfish': 5,
'trees': 3,
'cars': 2,
'perfumes': 1
}

def part_2_condition(prop, aunt, num):
    if prop == 'cats' or prop == 'trees':
        return aunt[prop] < num
    elif prop == 'pomeranians' or prop == 'goldfish':
        return aunt[prop] > num
    else:
        return aunt[prop] == num

for line in lines:
    _, name, prop1, num1, prop2, num2, prop3, num3 = line.split()
    num1 = int(num1[:-1])
    num2 = int(num2[:-1])
    num3 = int(num3)
    prop1 = prop1[:-1]
    prop2 = prop2[:-1]
    prop3 = prop3[:-1]

    if aunt[prop1] == num1 and aunt[prop2] == num2 and aunt[prop3] == num3:
        print('part 1:',name[:-1])
    if part_2_condition(prop1, aunt, num1) and part_2_condition(prop2, aunt, num2) and part_2_condition(prop3, aunt, num3):
        print('part 2:',name[:-1])
