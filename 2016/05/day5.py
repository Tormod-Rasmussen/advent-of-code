#--- Day 5: How About a Nice Game of Chess? ---
from hashlib import md5
import sys

with open('2016/05/input.txt') as f:
    input = f.readline()

index = 0
p1 = [None]*8
p2 = [None]*8
while None in p2 or None in p1:
    hash = md5((input+str(index)).encode('utf-8')).hexdigest()
    if None in p1 and hash[:5] == '00000':
        p1[p1.index(None)] = hash[5]
    if hash[:5] == '00000' and hash[5] in '01234567' and not p2[int(hash[5])]:
            p2[int(hash[5])] = hash[6]
    index += 1

    # cinematic "decrypting" animation
    if index % 10000 == 0: # limit writes
        sys.stdout.write('\rpart 1: ' + ''.join(
            p1[c] if p1[c] else hash[c] for c in range(8))+
            ' part 2: ' + ''.join(
            p2[c] if p2[c] else hash[c] for c in range(len(p2))))
sys.stdout.write('\r\033[K')
print('part 1: '+''.join(i for i in p1))
print('part 2: '+''.join(i for i in p2))
