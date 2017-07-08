'''
You have two numbers represented by a linked list, where each node contains a single digit. The digits are stored in reverse order, such that the 1's digit is at the head of the list. Write a function that adds the two numbers and returns the sum as a linked list.
EXAMPLE
Input: (3 -> 1 -> 5) + (5 -> 9 -> 2)
Output: 8 -> 0 -> 8
'''


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


class LinkifyElements(object):

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
            print iterator.getData(),
            iterator = iterator.next

    def returnHead(self):
        return self.head

    def returnLength(self):
        length = 0

        iterator = self.head

        while iterator is not None:
            iterator = iterator.next
            length = length + 1

        return length


class AddElementsOfLinkedList(object):
    def __init__(self, head1, head2, length1, length2):
        self.head1 = head1
        self.head2 = head2
        self.length1 = length1
        self.length2 = length2
        self.head = None

    def _addElements(self, carry , node1 , node2):
        value = carry
        lastValue = 0

        if node1 is None and node2 is None and carry == 0:
            return
        elif node1 is None and node2 is None and carry != 0 :
            nodeCarry = Node(carry)
            lastValue = 1

        if node1 is not None:
            value = value + node1.getData()
        elif node1 is None:
            value = value + 0

        if node2 is not None:
            value = value + node2.getData()
        elif node2 is None:
            value = value + 0

        node = Node(0)
        node.setData(value % 10)
        if value > 10 :
            carry = 1
        else:
            carry = 0

        if lastValue == 0:
            node.next = self._addElements(carry, node1.next , node2.next)
        elif lastValue == 1:
            node.next = nodeCarry

        return node


    def addElements(self):
        self._addElements(0 , self.head1, self.head2)



if __name__ == "__main__":
    linkify = LinkifyElements()
    # adding first number
    linkify.addElement(3)
    linkify.addElement(1)
    linkify.addElement(5)
    linkify.printLinkedList()

    lenght1 = linkify.returnLength()

    firsthead = linkify.returnHead()


    # adding Second Number
    linkify2 = LinkifyElements()
    linkify2.addElement(9)
    linkify2.addElement(9)
    print "\n"

    linkify2.printLinkedList()

    length2 = linkify2.returnLength()

    secondHead = linkify2.returnHead()


    addElem = AddElementsOfLinkedList(firsthead, secondHead, lenght1 , length2)
    addElem.addElements()


