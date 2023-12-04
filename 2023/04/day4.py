#--- Day 4: Scratchcards ---

with open('2023/04/input.txt') as f:
    lines = [[list(map(int, p.split())) for p in line.split(': ')[1].split(' | ')]
              for line in f.read().splitlines()]

total_points = 0
for line in lines:
    points = 0
    winning_nums, nums = line
    for n in nums:
        if n in winning_nums:
            points = points * 2 if points else points + 1
    total_points += points

print('part 1:',total_points)

num_cards = [1 for _ in range(len(lines))]
for i in range(len(lines)):
    winning_nums, nums = lines[i]
    win_count = sum(n in winning_nums for n in nums)
    for j in range(1,win_count+1):
        num_cards[i+j] += 1 * num_cards[i]

total_cards = sum(num_cards)
print('part 2:',total_cards)
