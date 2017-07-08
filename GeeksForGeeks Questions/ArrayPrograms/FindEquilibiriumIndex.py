def findEquilibiriumIndex(listOfElements):

    rightSum = 0
    leftSum = 0

    leftIterator = 0
    rightIterator = len(listOfElements) -1

    for element in listOfElements:
        rightSum = rightSum + element



    for index in range(0 , len(listOfElements)):
        rightSum = rightSum - listOfElements[index]

        if rightSum == leftSum:
            return index

        leftSum = leftSum + listOfElements[index]


findEquilibiriumIndex([-7, 1, 5, 2, -4, 3, 0])