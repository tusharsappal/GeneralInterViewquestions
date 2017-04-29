# This script checks if the expression  has the equal parenthesis
# We will be pushing the '(' and all operands  '+', '-', 'a' etc.
# When we encountered ')', we will be popping out the elements till we encounter '('
# if the string has balanced parenthesis we will be having an empty array at last , if not
# we have un equal parenthesis


class EqualParanthesis(object):

    def createStack(self):
        stack = []
        return stack

    def pushElement(self, stack, element):
        stack.append(element)

    def popElement(self, stack):
        if len(stack) == 0:
            print "Stack Underflow, cannot pop elements"
            return -1
        else:
            stack.pop()
            return


        # elif stack[-1] is '(':
        #     print "Encountered ( , not popping but pushing "
        #     return 0
        # else:
        #     stack.pop()
        #     self.popElement(stack)

    def equalParanthesis(self):
        stack = self.createStack()
        # Taking input from the user
        input_list = raw_input("Enter expression")
        #input_list = string_input.split()

        for index in range(0, input_list.__len__()):
            if input_list[index] is '(':
                self.pushElement(stack,input_list[index])
            elif input_list[index] is ')' :
                self.popElement(stack)

        # Now all elements are pushed , we will be checking equality

        if len(stack) is 0:
            print "The expression has equal paranthesis"
        else:
            print "The expression does not have equal paranthesis"

if __name__=="__main__":
    EqualParanthesis().equalParanthesis()