#--- Day 10: Balance Bots ---

with open('2016/10/input.txt') as f:
    lines = f.read().splitlines()

bots = dict()           #{bot:[item1,item2]}
instructions = dict()   #{bot:[to,low,to,high]}
outputs = dict()        #{output:item}
part1 = False

# instructions
for line in lines:
    if line.startswith('b'):
        line = line.split()
        instructions.update({int(line[1]):[line[5],int(line[6]),line[-2],int(line[-1])]})
        bots[int(line[1])] = []
# starting values
for line in lines:
    if line.startswith('v'):
        line = line.split()
        bots[int(line[-1])].append(int(line[1]))

def move_items(bot,items):
    # moves low / high items from bot following instructions
    low, high = sorted([items.pop(),items.pop()])
    if instructions[bot][0] == 'bot':
        bots[instructions[bot][1]].append(low)
    else:
        outputs[instructions[bot][1]] = low
    if instructions[bot][2] == 'bot':
        bots[instructions[bot][3]].append(high)
    else:
        outputs[instructions[bot][3]] = high

# move items while there are bots with 2 items
while any(len(item) > 1 for item in bots.values()):
    for bot,items in bots.items():
        if len(items) == 2:
            if 61 in items and 17 in items:
                part1 = bot
            move_items(bot,items)

print('part 1:',part1)
print('part 2:',outputs[0]*outputs[1]*outputs[2])
