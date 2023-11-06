#--- Day 1: Inverse Captcha ---

with open('2017/01/input.txt') as f:
    line = f.readline()

digits = list(line)
sum_digits = 0
for i in range(len(digits)-1):
    if digits[i] == digits[i+1]:
        sum_digits += int(digits[i])
if digits[0] == digits[-1]:
    sum_digits += int(digits[0])

print('part 1:',sum_digits)

sum_digits = 0
digits = 2*digits
for i in range(len(digits)//2):
    if digits[i] == digits[i+(len(digits)//4)]:
        sum_digits += int(digits[i])

print('part 2:',sum_digits)
