class SegregateEvenAndOdd(object):

    def segregateEvenAndOdd(self, listOfNumbers):

        leftPointer = 0
        rightPointer = len(listOfNumbers) - 1

        while leftPointer < rightPointer:

            if listOfNumbers[leftPointer] %2 == 0 :
                leftPointer = leftPointer + 1

            elif listOfNumbers[rightPointer] %2 != 0 :
                rightPointer = rightPointer - 1

            elif listOfNumbers[leftPointer]%2 != 0 and listOfNumbers[rightPointer]%2 == 0 :
                temp = listOfNumbers[leftPointer]
                listOfNumbers[leftPointer] = listOfNumbers[rightPointer]
                listOfNumbers[rightPointer] = temp
                leftPointer = leftPointer +1
                rightPointer = rightPointer - 1


        print listOfNumbers[::]


if __name__ == "__main__":
    listOfNumbers = [12, 34, 45, 9, 8, 90, 3]
    segg = SegregateEvenAndOdd()
    segg.segregateEvenAndOdd(listOfNumbers)
