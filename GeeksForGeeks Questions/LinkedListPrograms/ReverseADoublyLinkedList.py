class Node(object):

    def __init__(self,initData):
        self.data = initData
        self.next = None
        self.previous = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def getPrevious(self):
        return self.previous

    def setData(self,newData):
        self.data = newData

    def setNext(self,nextNode):
        self.next  = nextNode

    def setPrevious(self, previousNode):
        self.previous = previousNode

class ReverseDoublyLinkedList(object):

    head = None
    tail = None

    def __init__(self):
        self.head = None
        self.tail = None

    def isEmpty(self):
        return self.head is None and self.tail is None

    def insertElement(self, data):

        node = Node(data)

        if self.isEmpty():
            self.head = node
            self.tail = node
            node.next = self.tail
            node.previous = self.head
        else:
            node.previous = self.tail
            node.next = None
            self.tail.next = node
            self.tail = node

    def deleteElementFromStart(self):

        if self.isEmpty():
            print "Cannot delete the element as LinkedList is Empty"
        else:
            self.head = self.head.next
            self.head.next.previous = self.head


    def printLinkedList(self):

        if self.head == None and self.tail == None:
            print "The Linked List is Empty and cannot be traversed"
        else:
            iterator = self.head

            while iterator is not None:
                print iterator.getData()
                iterator= iterator.next

    def revereLinkedList(self):

        if self.isEmpty():
            print "Linked List is Empty and cannot reverse it"
        else:
            iterator = self.head
            tempNode = None

            while iterator is not None:
                tempNode = iterator.previous
                iterator.previous = iterator.next
                iterator.next = tempNode
                iterator = iterator.previous

            if tempNode is not  None:
                self.head  = tempNode.previous


if __name__=="__main__":
    doublyLinkedList = ReverseDoublyLinkedList()
    doublyLinkedList.insertElement(1)
    doublyLinkedList.insertElement(2)
    doublyLinkedList.insertElement(3)
    doublyLinkedList.insertElement(4)
    doublyLinkedList.insertElement(5)

    doublyLinkedList.printLinkedList()

    # Now we will be trying to reverse the linkedlist

    doublyLinkedList.revereLinkedList()



    # Now we will try to print the elements

    doublyLinkedList.printLinkedList()


