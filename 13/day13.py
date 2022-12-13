signals = open("13/input.txt").read().split("\n\n")

def compare(left,right,top): # returns True if right is bigger than left
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
    return True if top else "cont" # if comparing from main return True, else continue comparing

rightOrder = 0
for pair in range(len(signals)):
    left, right = signals[pair].split("\n")
    left, right = eval(left), eval(right)
    rightOrder += pair+1 if compare(left, right,1) else 0
print("part 1:",rightOrder)
