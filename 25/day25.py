lines = open("25/input.txt").read().splitlines()

def snafuToDecimal(number):
    decimal = 0
    for i in range(len(number)):
        if number[i] in "012":
            decimal += int(number[i]) * 5 ** (len(number) - i - 1)
        elif number[i] == "-":
            decimal -= 1 * 5 ** (len(number) - i - 1)
        elif number[i] == "=":
            decimal -= 2 * 5 ** (len(number) - i - 1)
    return decimal

def decimalToSnafu(number):
    snafu = ""
    while number != 0:
        remainder = number % 5
        if remainder == 0:
            snafu = "0" + snafu 
        elif remainder == 1:
            snafu = "1" + snafu
        elif remainder == 2:
            snafu = "2" + snafu
        elif remainder == 3:
            snafu = "=" + snafu
            number += 3
        elif remainder == 4:
            snafu = "-" + snafu
            number += 2
        number //= 5
    return snafu

sumOfSnafu = 0
for line in lines:
    sumOfSnafu += snafuToDecimal(line)
sumOfSnafu = decimalToSnafu(sumOfSnafu)
print("part 1:", sumOfSnafu)