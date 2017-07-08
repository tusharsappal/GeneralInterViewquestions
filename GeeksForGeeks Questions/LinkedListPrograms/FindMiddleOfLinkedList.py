# This program finds the middle of LinkedList
# Traverse linked list using two pointers.
# Move one pointer by one and other pointer by two. When the fast pointer reaches end slow pointer will reach middle of the linked list.

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

        else:
            # We will be pushing the data
            iterator = self.head
            while iterator.next is not None:
                iterator = iterator.next

            iterator.next = node

    def findMiddleNode(self):

        iterator = self.head
        iterator2 = self.head

        while iterator is not None and iterator2.next is not None:
            iterator = iterator.next
            iterator2 = iterator2.next.next


        print "The middle Node's data is %d" %(iterator.data)



if __name__ == "__main__":
    middElement = LinkedList()
    middElement.addElementsToLinkedList(1)
    middElement.addElementsToLinkedList(2)
    middElement.addElementsToLinkedList(3)
    middElement.addElementsToLinkedList(4)
    middElement.addElementsToLinkedList(5)
    middElement.addElementsToLinkedList(6)
    middElement.addElementsToLinkedList(7)
    middElement.findMiddleNode()

