
class Node(object):

    def __init__(self, dataElement):
        self.data = dataElement
        self.next = None

    def getElement(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self, newData):
        self.data = newData

    def setNext(self, nextNode):
        self.next = nextNode


class NthNode(object):
    global c
    c = 1

    def __init__(self):
        self.head = None


    def addElement(self, dataElement):
        node = Node(dataElement)

        if self.head is None:
            node.next = None
            self.head = node
        else:
            iterator = self.head
            while iterator.next is not None:

                iterator = iterator.next

            iterator.next = node
            node.next = None

    def deleteNNode(self, nodeIndexFromLast):
        self.nodeIndex  = nodeIndexFromLast
        self._deleteNNodeFromLast(self.head, nodeIndexFromLast)

    def _deleteNNodeFromLast(self, node , indexToBeDeleted):

        # Maintain the difference of nodeIndexFromLast between the
        iteratorA= self.head
        iteratorB = self.head
        index = 1
        while index <= indexToBeDeleted:
            iteratorB = iteratorB.next
            index = index +1

        # Now we have maintained the difference ,we will move both the nodes
        while iteratorB.next is not None:
            iteratorB = iteratorB.next
            iteratorA = iteratorA.next


        print "Removing Node with data value %d" %(iteratorA.next.data)
        iteratorA.next = iteratorA.next.next




    def printLinkedList(self):
        iterator = self.head

        while iterator is not None:
            print iterator.data,
            iterator = iterator.next


if __name__ == "__main__":
    list = NthNode()
    list.addElement(1)
    list.addElement(2)
    list.addElement(3)
    list.addElement(4)
    list.addElement(5)
    list.addElement(6)

    list.printLinkedList()

    list.deleteNNode(2)
    list.printLinkedList()

    # Now we will pass the value of the n node to be deleted







