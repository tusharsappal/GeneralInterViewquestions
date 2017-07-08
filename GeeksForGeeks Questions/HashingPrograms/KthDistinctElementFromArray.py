import collections

class KThDistinctElement(object):

    def printKthDistinctElement(self, kthElement):

        elementList = [2, 2, 2, 2]
        countDict= collections.OrderedDict()

        for element in elementList:
            if element in countDict:
                countDict[element] = countDict[element] + 1
            else:
                countDict[element] = 1

        currentDistinctCount = 0



        for element in elementList:
            if countDict[element] == 1 and currentDistinctCount != kthElement-1:
                currentDistinctCount = currentDistinctCount +1
            elif countDict[element] == 1 and currentDistinctCount == kthElement-1:
                print "The element is %d" %(element)
                break

        if currentDistinctCount != kthElement-1:
            print "-1"



if __name__ == "__main__":
    distinct = KThDistinctElement()
    #distinct = KThDistinctElement([])

    kthElement = raw_input("Enter Kth Element")
    kthElement = int(kthElement)
    distinct.printKthDistinctElement(kthElement)
