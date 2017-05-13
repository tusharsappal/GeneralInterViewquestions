class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next


class LinkedList(object):

    def __init__(self):
        self.head = None

    def isListEmpty(self):
        return self.head == None

    def addElement(self, value):
        node = Node(value)

        if self.isListEmpty():
            self.head = node
        else:
            iterator = self.head

            while iterator.getNext()!= None:
                iterator = iterator.next

            iterator.next = node

    def findMiddleNodeOfLinkedList(self):

        slowPointer = self.head
        fastPointer = self.head

        while fastPointer.next != None:
            slowPointer = slowPointer.next
            fastPointer = fastPointer.next.next


        return slowPointer

    def _compareStackandLinkedList(self, stackToPushElements):

        iterator = self.head
        while iterator is not None:
            if iterator.getData() == stackToPushElements.pop():
                iterator = iterator.getNext()
            else:
                return False

        return True


    def checkLinkedListisPalindrome(self):

        stackToPushElements = []

        iterator = self.head

        while iterator != None:
            stackToPushElements.append(iterator.data)
            iterator = iterator.next


        return self._compareStackandLinkedList(stackToPushElements)


if __name__ == "__main__":
    linkedlist = LinkedList()
    linkedlist.addElement(10)
    linkedlist.addElement(20)
    linkedlist.addElement(30)
    linkedlist.addElement(20)
    linkedlist.addElement(10)

    if linkedlist.checkLinkedListisPalindrome():
        print "LinkedList is Palindrome"
    else:
        print "linked list if not Palindrome"