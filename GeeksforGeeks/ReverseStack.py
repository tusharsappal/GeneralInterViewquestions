
class ReverseStack(object):

    def createStack(self):
        stack = []
        return stack

    def pushElement(self, stack , element):
        stack.append(element)

    def popElement(self,stack):
        if not stack:
            print "Stack underflow , not able to pop"
        else:
            stack.pop()

    def printStackTrace(self,stack):
        for index in range(len(stack)-1, -1, -1):
            print stack[index]

    def reverseStack(self,stack):
        mid = int(len(stack) / 2)
        for index in range(0, mid):
            temp = stack[index]
            stack[index] = stack[(len(stack)-1)- index]
            stack[(len(stack)-1)-index] = temp

        self.printStackTrace(stack)

    def implementor(self):
        stack = self.createStack()
        self.pushElement(stack,4)
        self.pushElement(stack,3)
        self.pushElement(stack,2)
        self.pushElement(stack,1)

        self.printStackTrace(stack)
        print "Reverse Stack Trace"
        self.reverseStack(stack)

        # Now we will be reversing the stack elements


if __name__=="__main__":
    ReverseStack().implementor()