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

class UnionIntersection(object):

    def __init__(self):
        self.headList1 = None
        self.headList2 = None

    def isFirstListEmpty(self):
        return self.headList1 == None

    def isSeconfListEmpty(self):
        return self.headList2 == None

    def addElememtsToFirstList(self, dataElement):
        node = Node(dataElement)

        if self.isFirstListEmpty():
            self.headList1 = node
        else:
            iterator = self.headList1

            while iterator.getNext() != None:
                iterator = iterator.getNext()
            iterator.next = node

    def addElememtsToSecondList(self, dataElement):
        node = Node(dataElement)

        if self.isSeconfListEmpty():
            self.headList2 = node
        else:
            iterator = self.headList2

            while iterator.next != None:
                iterator = iterator.getNext()
            iterator.next = node


    def printLinkedList1(self):
        if self.headList1 == None:
            print "Cannot traverse an empty LinkedList"
        else:
            iterator = self.headList1
            while iterator != None:
                print iterator.data,
                iterator = iterator.next

    def printLinkedList2(self):
        if self.headList2 == None:
            print "Cannot Traverse an empty LinkedList"
        else:
            iterator = self.headList2
            while iterator!= None:
                print iterator.data,
                iterator = iterator.next

    # We would be using the Hashmap approach ,
    def findUnionOfLinkedList(self):

        dict = {}

        iterator1 = self.headList1
        iterator2 = self.headList2
        index = 0


        while iterator1 != None:
            if iterator1.data in dict.values():
                iterator1 = iterator1.next
            else:
                dict[index]= iterator1.data
            iterator1 = iterator1.next
            index = index +1

        print "Index is %d" %(index)

        while iterator2 != None:
            if iterator2.data in dict.values():
                iterator2 = iterator2.next
            else:
                dict[index] = iterator2.data
            iterator2 = iterator2.next
            index = index +1

        print "\nUnion of two LinkedList is"
        for key,value in dict.items():
            print value



        # while iterator1 != None or iterator2 != None:
        #     if iterator1.data not in dict:
        #         dict[index] = iterator1.data
        #     else:
        #         dict[index] = iterator2.data
        #
        #     iterator1 = iterator1.next
        #     iterator2 = iterator2.next
        #     index = index+1
        #

        # Now printing the Dictionary






if __name__ == "__main__":
    unionIntersection = UnionIntersection()
    unionIntersection.addElememtsToFirstList(10)
    unionIntersection.addElememtsToFirstList(15)
    unionIntersection.addElememtsToFirstList(4)
    unionIntersection.addElememtsToFirstList(20)

    # populating the second linkedlist

    unionIntersection.addElememtsToSecondList(8)
    unionIntersection.addElememtsToSecondList(4)
    unionIntersection.addElememtsToSecondList(2)
    unionIntersection.addElememtsToSecondList(0)


    # Printing the first linkedList
    print "First LinkedList is "
    unionIntersection.printLinkedList1()
    # Printing the seconf LinkedList
    print "\nSecond LinkedList is"
    unionIntersection.printLinkedList2()

    unionIntersection.findUnionOfLinkedList()

