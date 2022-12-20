lines = open("07/input.txt").read().splitlines()
folders = {} # every folder and its contents
path = "" # folder path (tracking full path because system has duplicate names in different paths)
for line in lines:
    if line.startswith("$ ls"):
        continue
    elif line.startswith("$ cd"):
        if line.endswith(".."):
            path = path.rsplit(" ",1)[0] # go up a folder
        else:
            path += " " + line.split(" ")[2] # go into a folder
            folders[path] = [] # add folder to dictionary
    else:
        try: # if it's a file, add its size
            folders[path].append(int(line.split(" ")[0]))
        except ValueError: # if it's a folder, add its name
            folders[path].append(line.split(" ")[1])

def findFolderSize(folder):
    folderSize = 0
    content = folders[folder]
    for item in content:
        if type(item) == int: # if it's a file, add its size
            folderSize += item
        else:               # if it's a folder, call the function on it
            folderSize += findFolderSize(folder + " " + item)
    return folderSize

sumSmallFolders = 0
sumAllFiles = findFolderSize(" /") # sum of files in root folder
spaceNeeded = 30000000 - (70000000 - sumAllFiles)
smallestDelFolder = sumAllFiles

for folder in folders:
    size = findFolderSize(folder)
    # part 1: sum of folders smaller than 100000
    sumSmallFolders += size if size <= 100000 else 0
    # part 2: find smallest folder that can be deleted
    if spaceNeeded <= size < smallestDelFolder:
        smallestDelFolder = size
print("part 1:",sumSmallFolders)
print("part 2:",smallestDelFolder)