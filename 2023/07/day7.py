#--- Day 7: Camel Cards ---
from collections import Counter

with open('2023/07/input.txt') as f:
    lines = f.read().splitlines()
part2=False
hands = []
for line in lines:
    hand,bid = line.split()
    bid = int(bid)
    hands.append([hand,bid])

def replace_j(hand):
    if hand == 'JJJJJ':
        return [5]
    common = Counter(hand).most_common(2)
    hand = hand.replace('J',common[0][0] if common[0][0] != 'J' else common[1][0])
    return list(Counter(hand).values())

def hand_rank(hand):
    if part2:
        hand = replace_j(hand)
    else:
        hand = list(Counter(hand).values())
    if 5 in hand:
        return 6 # 5 of a kind
    if 4 in hand:
        return 5 # 4 of a kind
    if 3 in hand and 2 in hand:
        return 4 # full house
    if 3 in hand:
        return 3 # 3 of a kind
    if hand.count(2) == 2:
        return 2 # two pairs
    if 2 in hand:
        return 1 # one pair
    return 0 # high card

# compare hand for sorting
def compare_hand(one,two):
    # returns true if low is a worse hand than high
    low_rank, high_rank = hand_rank(one[0]), hand_rank(two[0])
    if low_rank > high_rank:
        return
    if high_rank > low_rank:
        return True
    card_value = {'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'T':10,'J':11,'Q':12,'K':13,'A':14}
    if part2:
        card_value['J'] = 1
    for card in range(5):
        if card_value[one[0][card]] > card_value[two[0][card]]:
            return
        if card_value[two[0][card]] > card_value[one[0][card]]:
            return True

def bubble_sort(array):
    n = len(array)
    for i in range(n):
        already_sorted = True
        for j in range(n - i - 1):
            if compare_hand(array[j + 1],array[j]):
                # if j+1 is worse than j, swap them
                array[j], array[j + 1] = array[j + 1], array[j]
                already_sorted = False
        # If there were no swaps, it's sorted
        if already_sorted:
            break
    return array

def get_total(hands):
    hands = bubble_sort(hands)
    total = 0
    for i in range(len(hands)):
        total += hands[i][1]*(i+1)
    return total

print('part 1:',get_total(hands))
part2=True
print('part 2:',get_total(hands))
