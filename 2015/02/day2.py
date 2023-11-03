#--- Day 2: I Was Told There Would Be No Math ---

with open("2015/02/input.txt") as f:
    lines = f.read().splitlines()
wrappingPaper = 0
ribbon = 0
for line in lines:
    line = line.split("x")
    line = [int(i) for i in line]
    line.sort()
    width, length, height = [int(i) for i in line]
    wrappingPaper += (
        2*width*length +
        2*length*height +
        2*height*width +
        width * length
    )
    ribbon += (
        width * 2 +
        length * 2 +
        width * length * height
    )
print("part 1:",wrappingPaper)
print("part 2:",ribbon)
