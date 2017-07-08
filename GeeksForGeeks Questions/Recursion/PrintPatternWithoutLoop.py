# Print a pattern without a loop
#Input: n = 16
#Output: 16, 11, 6, 1, -4, 1, 6, 11, 16

#Input: n = 10
#Output: 10, 5, 0, 5, 10


def printPatternUsingRecursion(number):

    if number <= 0:
        print number
        return

    print number
    printPatternUsingRecursion(number-5)
    print number


printPatternUsingRecursion(16)