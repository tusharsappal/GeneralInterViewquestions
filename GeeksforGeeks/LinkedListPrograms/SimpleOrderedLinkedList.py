
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

class OrderedList(object):

    head = None

    def __int__(self):
        self.head = None

    def isEmpty(self):
        return self.head is None

    def addElementToOrderedList(self, element):

        node = Node(element)
        node.next = None

        if self.isEmpty():
            self.head = node
        else :
            iterator = self.head
            while iterator.getNext() is not None:
                iterator = iterator.next
            iterator.next = node

    def printOrderedList(self):
        iterator = self.head
        while iterator is not None:
            print iterator.getData()
            iterator = iterator.getNext()



if __name__=="__main__":

    print "Now Ordered List Operations Starts"

    orderedList = OrderedList()
    orderedList.addElementToOrderedList(10)
    orderedList.addElementToOrderedList(20)
    orderedList.addElementToOrderedList(30)
    orderedList.addElementToOrderedList(40)
    orderedList.addElementToOrderedList(50)
    orderedList.addElementToOrderedList(60)
    orderedList.addElementToOrderedList(70)

    orderedList.printOrderedList()

