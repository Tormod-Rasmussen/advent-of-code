#--- Day 20: Infinite Elves and Infinite Houses ---

with open('2015/20/input.txt') as f:
    num = int(f.read())

# brute force solution
houses = [0]*(num//10)
for elf in range(1, num//10):
    #each elf adds their presents to each house they visit
    for house in range(elf, num//10, elf):
        houses[house] += elf*10
    # when the house has more presents than the input, we have the answer
    if houses[elf] >= num:
        print('part 1:',elf)
        break

# basically same as part 1
houses = [0]*(num//10)
for elf in range(1, num//10):
    for house in range(elf, min(num//10, elf*50+1), elf):
        houses[house] += elf*11
    if houses[elf] >= num:
        print('part 2:',elf)
        break
