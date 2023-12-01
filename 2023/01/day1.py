#--- Day 1: Trebuchet?! ---
import re

with open('2023/01/input.txt') as f:
    lines = f.read().splitlines()

def replace_text(line):
    # keeping first and last letters to get both numbers from overlapping words
    line = line.replace('one','o1e').replace('two','t2o').replace('three','t3e')
    line = line.replace('four','f4r').replace('five','f5e').replace('six','s6x')
    line = line.replace('seven','s7n').replace('eight','e8t').replace('nine','n9e')
    return line

def find_calibration_values(part2=False):
    total = 0
    for line in lines:
        if part2:
            line = replace_text(line)
        nums = re.findall(r'\d',line)
        total += int(nums[0]+nums[-1])
    return total

print('part 1:',find_calibration_values())
print('part 2:',find_calibration_values(True))
