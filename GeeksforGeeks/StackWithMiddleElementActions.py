'''How to implement a stack which will support following operations in O(1) time complexity?
1) push() which adds an element to the top of stack.
2) pop() which removes an element from top of stack.
3) findMiddle() which will return middle element of the stack.
4) deleteMiddle() which will delete the middle element.
Push and pop are standard stack operations.'''

class MiddleElemetOperationImplementor(object):

    def createStack(self):
        stack = []
        return stack

    def pushElement(self, stack, element):
        stack.append(element)

    def popElement(self, stack, element):
        if len(stack) == 0:
            print "Stack Underflow, cannot pop elements"
            return -1
        else:
            stack.pop()

    def returnMiddleElementOfStack(self,stack):
        return stack[int(len(stack)/2)]

    def deleteMiddleElement(self,stack):

        middle_index = int(len(stack)/2)

        for index in range(middle_index,len(stack)-1):
            stack[index] = stack[index+1]

        # Now printing the Stack with Middle Element Deleted
        for index in range(len(stack)-2, -1, -1):
            print stack[index]


    def printStackTrace(self,stack):

        for index in range(len(stack)-1, -1, -1):
            print stack[index]

    def implementor(self):
        stack = self.createStack()
        self.pushElement(stack,5)
        self.pushElement(stack,4)
        self.pushElement(stack,3)
        self.pushElement(stack,2)
        self.pushElement(stack,1)
        self.printStackTrace(stack)
        # Printing the Middle Element
        print "The Middle Element of Stack is %d" %(self.returnMiddleElementOfStack(stack))
        self.deleteMiddleElement(stack)


if __name__=="__main__":
    MiddleElemetOperationImplementor().implementor()

