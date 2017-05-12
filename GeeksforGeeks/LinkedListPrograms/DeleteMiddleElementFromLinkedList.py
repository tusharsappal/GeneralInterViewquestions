
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

class LinkedList(object):

    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head is None

    def addElementsToLinkedList(self, element):
        node = Node(element)

        if self.isEmpty():
            self.head = node

        else:
            # We will be pushing the data
            iterator = self.head
            while iterator.next is not None:
                iterator = iterator.next

            iterator.next = node

    def deleteMiddleELement(self):
        # The conecpt we will be using is of slow pointer and fast pointer
        # Slow pointer will be increased by 1 step and fast pointer will be increased by 2 steps
        # When the fast pointer will be at last , slow pointer will be in the middle
        fastPtr = self.head
        slowPtr = self.head
        prevNode = None

        while fastPtr.next != None:
            fastPtr = fastPtr.next.next
            prevNode = slowPtr
            slowPtr = slowPtr.next


        prevNode.next = slowPtr.next
        slowPtr = None


    def printOrderedList(self):
        iterator = self.head
        while iterator is not None:
            print iterator.getData()
            iterator = iterator.getNext()



if __name__=="__main__":

    print "Now Ordered List Operations Starts"

    orderedList = LinkedList()
    orderedList.addElementsToLinkedList(10)
    orderedList.addElementsToLinkedList(20)
    orderedList.addElementsToLinkedList(30)
    orderedList.addElementsToLinkedList(40)
    orderedList.addElementsToLinkedList(50)

    # Before removing middle element
    print "before removing middle elment \n"
    orderedList.printOrderedList()

    print "After deleting the middle element \n"
    orderedList.deleteMiddleELement()
    orderedList.printOrderedList()