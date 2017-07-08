class Node(object):

    def __init__(self,initData):
        self.data = initData
        self.next = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self,newData):
        self.data = newData

    def setNext(self,nextNode):
        self.next  = nextNode


class RemoveDuplicatesFromLinkedList(object):

    def __init__(self):
        self.head = None

    def isListEmpty(self):
        return self.head == None

    def addElement(self, numberToBeAdded):

        node = Node(numberToBeAdded)
        node.next = None


        if self.isListEmpty():
            self.head = node
        else:
            iteraor = self.head

            while iteraor.next is not None:
                iteraor = iteraor.next

            iteraor.next = node


    def printLinkedList(self):

        iterator = self.head
        while iterator is not None:
            print iterator.getData()
            iterator = iterator.next

    def removeDuplicateElements(self):
        iterator = self.head
        if self.head == None:
            print "Empty List"
            return -1
        else:
            hasSet = set()
            previous = None

            while iterator is not None:
                if hasSet.__contains__(iterator.getData()):
                    previous.next = iterator.next
                else:
                    hasSet.add(iterator.getData())
                    previous = iterator
                iterator = iterator.next



if __name__ == "__main__":
    removeDups = RemoveDuplicatesFromLinkedList()
    removeDups.addElement(12)
    removeDups.addElement(11)
    removeDups.addElement(12)
    removeDups.addElement(21)
    removeDups.addElement(41)
    removeDups.addElement(43)
    removeDups.addElement(21)

    removeDups.printLinkedList()

    removeDups.removeDuplicateElements()
    print "--------------"

    removeDups.printLinkedList()