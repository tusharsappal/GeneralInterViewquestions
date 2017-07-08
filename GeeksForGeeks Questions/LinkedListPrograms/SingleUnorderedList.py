# This program implements the Singly Unordered LinkedList in Python

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


# Since we are implementing the UnOrdered List , the first element to be inserted would eventually be the last Element
# As the order does not matter , so we will try to implement it like a Stack Data Structure

class UnOrderedList(object):
    head = None

    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head == None

    def add(self, itemToBeAdded):

        node = Node(itemToBeAdded)
        node.next = None
        if self.isEmpty():

            self.head = node
        else:
            node.next = self.head
            self.head = node
            # iterator = self.head
            # while iterator.getNext() is not None:
            #     iterator = iterator.next

            # iterator.next = node

    # We will be printing the UnOrdered List from the start to the End.
    def printUnOrderedList(self):
        iterator = self.head
        while iterator is not None:
            print iterator.getData()
            iterator = iterator.getNext()


if __name__=="__main__":
    unorderedList = UnOrderedList()
    unorderedList.add(10)
    unorderedList.add(20)
    unorderedList.add(30)
    unorderedList.add(40)
    unorderedList.add(50)
    unorderedList.add(60)
    # Now we will be printing the un Ordered List

    unorderedList.printUnOrderedList()

