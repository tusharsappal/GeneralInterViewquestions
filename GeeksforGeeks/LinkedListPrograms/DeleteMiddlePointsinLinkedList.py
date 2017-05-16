class Node(object):

    def __init__(self,listOfData):
        self.data = listOfData
        self.next = None

    def getData(self):
        return self.data[::]

    def getNext(self):
        return self.next

    def setData(self,newData):
        self.data = newData

    def setNext(self,nextNode):
        self.next  = nextNode


class DeleteMiddlePoints(object):
    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head == None

    def addNodesToLinkedList(self, listOfData):

        node = Node(listOfData)
        node.next = None

        if self.isEmpty():
            self.head = node
        else:
            iterator = self.head

            while iterator.next != None:
                iterator = iterator.getNext()

            iterator.next = node


    def deleteMiddlePoints(self):

        current = self.head
        nextNode = current.getNext()
        nextNextNode = nextNode.getNext()

        while nextNextNode.getNext() != None:
            nextNode = current.getNext()
            nextNextNode = nextNode.getNext()
            if current.getData()[1] == nextNode.getData()[1] == nextNextNode.getData()[1] or current.getData()[0] == nextNode.getData()[0] == nextNextNode.getData()[0]:
                current.next = nextNextNode
            else:
                current = current.next


    def printLinkedList(self):
        iterator = self.head
        while iterator != None:
            print iterator.getData()
            iterator = iterator.getNext()


if __name__ == "__main__":
    deleteNode = DeleteMiddlePoints()
    deleteNode.addNodesToLinkedList([0, 10])
    deleteNode.addNodesToLinkedList([1, 10])
    deleteNode.addNodesToLinkedList([3, 10])
    deleteNode.addNodesToLinkedList([10, 10])
    deleteNode.addNodesToLinkedList([10, 8])
    deleteNode.addNodesToLinkedList([10, 5])
    deleteNode.addNodesToLinkedList([20, 5])
    deleteNode.addNodesToLinkedList([40, 5])

    deleteNode.printLinkedList()

    # Now we are trying to delete some nodes which are middle nodes

    deleteNode.deleteMiddlePoints()
    print "After Deleting the Nodes which have common entries"

    deleteNode.printLinkedList()

