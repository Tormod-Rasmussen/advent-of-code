#--- Day 11: Corporate Policy ---

with open('2015/11/input.txt') as f:
    password = f.readline()

def rule1(password):
    for i in range(len(list(password)) - 2):
        if password[i:i+3] in 'abcdefghijklmnopqrstuvwxyz':
            return True

def rule2(password):
    return all(i not in password for i in 'iou')

def rule3(password):
    pairs = 0
    i = 0
    while i < len(password)-1:
        if password[i] == password[i+1]:
            pairs += 1
            i += 1
        i += 1
    return True if pairs > 1 else False

def increment_pass(password):
    data = list(password)
    for i in range(len(data)-1,-1,-1):
        data[i] = chr((ord(data[i]) - ord('a') + 1) % 26 + ord('a'))
        if data[i] != 'a':
            break
    return ''.join(data)

def next_valid_pass(current_password):
    rules = [rule1, rule2, rule3]
    password = increment_pass(current_password)
    while not all((func(password) for func in rules)):
        password = increment_pass(password)
    return password

password = next_valid_pass(password)
print('part 1:',password)
password = next_valid_pass(password)
print('part 2:',password)
