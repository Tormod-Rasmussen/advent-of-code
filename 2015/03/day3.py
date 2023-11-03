#--- Day 3: Perfectly Spherical Houses in a Vacuum ---

with open("2015/03/input.txt") as f:
    string = f.readline()
x = 0
y = 0
coordinates = {(str(x)+","+str(y))}
for i in range(len(string)):
    if string[i] == "^":
        y += 1
    elif string[i] == "v":
        y-= 1
    elif string[i] == ">":
        x += 1
    elif string[i] == "<":
        x -= 1
    coordinates.add(str(x)+","+ str(y))
print("part 1:",len(coordinates))

x = 0
y = 0
coordinates = {(str(x)+","+str(y))}
robotX = 0
robotY = 0
robotCoordinates = {(str(robotX)+","+str(robotY))}
for i in range(len(string)):
    if i % 2 == 0:
        if string[i] == "^":
            y += 1
        elif string[i] == "v":
            y-= 1
        elif string[i] == ">":
            x += 1
        elif string[i] == "<":
            x -= 1
        coordinates.add(str(x)+","+ str(y))
    else:
        if string[i] == "^":
            robotY += 1
        elif string[i] == "v":
            robotY-= 1
        elif string[i] == ">":
            robotX += 1
        elif string[i] == "<":
            robotX -= 1
        robotCoordinates.add(str(robotX)+","+ str(robotY))
coordinates.update(robotCoordinates)
print("part 2:",len(coordinates))
