# This program deletes the Node from the given position from the LinkedList

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

    def printELementsOfNode(self):

        if self.isEmpty():
            print "Cannot print the elements , The LinkedList is Empty"
        else:
            iterator = self.head
            while iterator is not None:
                print iterator.data
                iterator= iterator.next

    def countLengthOfLinkedListViaRecursion(self, node):

        if node is None:
            return 0
        else:
            count = 1 + self.countLengthOfLinkedListViaRecursion(node.next)
            return count

    def getCount(self):
        count = self.countLengthOfLinkedListViaRecursion(self.head)
        return count


if __name__=="__main__":

    linkedList = LinkedList()
    linkedList.addElementsToLinkedList(10)
    linkedList.addElementsToLinkedList(20)
    linkedList.addElementsToLinkedList(30)
    linkedList.addElementsToLinkedList(40)
    linkedList.addElementsToLinkedList(50)

    # Now printing the element

    linkedList.printELementsOfNode()

    # Now we will be printing the count of the LinkedList
    print "Count is %d " %(linkedList.getCount())