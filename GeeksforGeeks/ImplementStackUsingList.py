
class StackImplementationUsingList(object):

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

    def implementor(self):
        stack = self.createStack()
        self.pushElement(stack,4)
        self.pushElement(stack,3)
        self.pushElement(stack,2)
        self.pushElement(stack,1)

        self.printStackTrace(stack)

        print "Now Poppping Begins "

        self.popElement(stack)
        self.popElement(stack)
        self.popElement(stack)
        self.printStackTrace(stack)
        self.popElement(stack)

        # Now this should fail
        self.popElement(stack)




if __name__=="__main__":
    StackImplementationUsingList().implementor()