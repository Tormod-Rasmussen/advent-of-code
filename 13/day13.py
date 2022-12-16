signals = open("13/input.txt").read().split("\n\n")

def compare(left,right,top): # top is False if comparing from within the function
    for i in range(max(len(right), len(left))):
        try:
            if type(left[i]) == int and type(right[i]) == int:
                if left[i] < right[i]:
                    # print("right is bigger when comparing", left[i], "and", right[i], "in", left, "and", right)
                    return True
                if left[i] > right[i]:
                    # print("left is bigger when comparing", left[i], "and", right[i], "in", left, "and", right)
                    return False
            elif type(left[i]) == list and type(right[i]) == list:
                if compare(left[i],right[i],0) == True:
                    return True
                elif compare(left[i],right[i],0) == False:
                    return False
            elif type(left[i]) == list and type(right[i]) == int:
                if compare(left[i],[right[i]],0) == True:
                    return True
                elif compare(left[i],[right[i]],0) == False:
                    return False
            elif type(left[i]) == int and type(right[i]) == list:
                if compare([left[i]],right[i],0) == True:
                    return True
                elif compare([left[i]],right[i],0) == False:
                    return False
        except IndexError:
            if len(left) > len(right):
                # print("right side ran out of items when comparing:", left," and ", right)
                return False
            else:
                # print("left side ran out of items when comparing:", left," and ", right)
                return True
    return True if top else "" # if comparing from outside function return True, else continue comparing

rightOrder = 0
for pair in range(len(signals)):
    left, right = signals[pair].split("\n")
    left, right = eval(left), eval(right)
    rightOrder += pair+1 if compare(left, right,1) else 0
print("part 1:",rightOrder)

ordered = [[[2]],[[6]]]
for line in open("13/input.txt").read().split("\n"):
    if line != "": # add all packets to list
        ordered += [eval(line)]
for i in range(len(ordered)): # compare all packets to each other
    for j in range(len(ordered)):
        if compare(ordered[i],ordered[j],0) == True:        # if right is bigger than left
            ordered[i], ordered[j] = ordered[j], ordered[i] # swap
dividerPackets = (ordered.index([[2]])+1) * (ordered.index([[6]])+1)

print("part 2:",dividerPackets)
