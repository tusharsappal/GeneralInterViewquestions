class CheckArrayIsSorted(object):

    def checkIfSortedIterative(self):
        inputA = raw_input("Enter the array elements separated by ,")
        inputList = inputA.split(',')
        inputList = [int(a) for a in inputList]

        for index in range(1,len(inputList)):
            if inputList[index] < inputList[index-1]:
                return  False
        return True

if __name__ == "__main__":
    checkArraySorted = CheckArrayIsSorted()
    if checkArraySorted.checkIfSortedIterative():
        print "Array is sorted"
    else:
        print "Array is not sorted"
