#--- Day 6: Memory Reallocation ---

with open('2017/06/input.txt') as f:
    line = f.readline()
blocks = [int(i) for i in line.split()]
seen_config = []
part1 = 0

def redistribute(blocks, num):
    to_distribute = blocks[num]
    blocks[num] = 0
    while to_distribute:
        num = 0 if num % (len(blocks)-1) == 0 and num != 0 else num+1
        blocks[num] += 1
        to_distribute -= 1
    return blocks

while True:
    if blocks in seen_config:
        break
    else:
        part1 += 1
        seen_config.append(blocks[:])
        blocks = redistribute(blocks,blocks.index(max(blocks)))
print('part 1:',part1)

seen_config = blocks[:]
blocks = [int(i) for i in line.split()]
part2 = 0

while blocks != seen_config:
    part2 += 1
    blocks = redistribute(blocks,blocks.index(max(blocks)))
print('part 2:',part1-part2)