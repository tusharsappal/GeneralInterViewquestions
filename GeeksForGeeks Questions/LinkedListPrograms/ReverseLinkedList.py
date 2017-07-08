class Node(object):

    def __init__(self, dataElement):
        self.data = dataElement
        self.next = None

    def getNodeData(self):
        return self.data

    def getNextNode(self):
        return self.next

    def setNodeData(self, newDataElement):
        self.data  = newDataElement

    def setNextNode(self, newNode):
        self.next = newNode


class LinkedList(object):

    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head is None

    def addElementsToLinkedList(self, element):
        node = Node(element)

        if self.isEmpty():
            self.head = node
            node.next = None
        else:
            # We will be pushing the data
            iterator = self.head
            while iterator.next is not None:
                iterator = iterator.next

            iterator.next = node

       # self.reverseLinkedList(self.head)


    def printLinkedListValues(self):
        iterator = self.head
        while iterator is not None:
            print iterator.data
            iterator = iterator.next

        # reversing the LinkedList now

        print "printing the Reversed Linkedlist"
        self.reverseLinkedList(self.head)



    def reverseLinkedList(self, node):

        if node.next is None:
            print node.data
        else:
            self.reverseLinkedList(node.next)
            print node.data

    def reverseLinkedListUsingIteration(self):
        self._reverseLinkedListUsingIteration(self.head)

    def _reverseLinkedListUsingIteration(self, node):

        if node is None:
            return
        else:
            prev = None
            current = node

            while current != None:
                next = current.next
                current.next = prev
                prev = current
                current = next
            self.head = prev

        print "Again the reverse LinkedList"
        self.printLinkedListValues()


if __name__ == "__main__":
    linkedList = LinkedList()
    linkedList.addElementsToLinkedList(1)
    linkedList.addElementsToLinkedList(2)
    linkedList.addElementsToLinkedList(3)
    linkedList.addElementsToLinkedList(4)
    linkedList.addElementsToLinkedList(5)
    linkedList.addElementsToLinkedList(6)

    linkedList.printLinkedListValues()

    # Now we will be reversing the linkedList using the iteration method

    linkedList.reverseLinkedListUsingIteration()





