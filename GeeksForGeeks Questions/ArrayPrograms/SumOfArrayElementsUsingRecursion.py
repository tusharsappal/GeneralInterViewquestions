class SumOfArrayRecursion(object):

    def _getSumOfElements(self, listOfElements, lenghtOflist ):

        if lenghtOflist == 0:
            return 0
        else:

            return  listOfElements[lenghtOflist-1] + self._getSumOfElements(listOfElements, lenghtOflist-1)

    def getSumOfElements(self, listOfElements):

        if len(listOfElements) == 1:
            print "Sum is %d " %listOfElements[0]
        else:
            print "Sum is %d "%(self._getSumOfElements(listOfElements, len(listOfElements)))
    

if __name__ == "__main__":
    listOfElements = [6, 5, 4, 3, 2, 1]
    sumOfArray = SumOfArrayRecursion()
    sumOfArray.getSumOfElements(listOfElements)