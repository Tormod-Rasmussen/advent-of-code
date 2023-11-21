#--- Day 4: Security Through Obscurity ---
from collections import Counter

with open('2016/04/input.txt') as f:
    lines = f.read().splitlines()

sum_id = 0
for line in lines:
    name, checksum = line.split('[')
    checksum = checksum[:-1]
    room_id = int(name.split('-')[-1])
    name = ''.join(name.split('-')[:-1])
    common_letters = ''.join(item[0] for item in Counter(sorted(name)).most_common(5))
    if common_letters == checksum:
        sum_id += room_id
print('part 1:',sum_id)

def decode_room_name(room, room_id):
    decoded_name = ''
    for letter in room:
        decoded_name += letter if letter == ' ' else chr((ord(letter)-97+room_id) % 26 + 97)
    return decoded_name

for line in lines:
    name, checksum = line.split('[')
    room_id = int(name.split('-')[-1])
    name = name[:-4].replace('-',' ')
    if decode_room_name(name,room_id) == 'northpole object storage':
        print('part 2:',room_id)
        break
