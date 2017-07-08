
class LengthEncoding(object):

    def __init__(self, stringPassed):
        self.inputString = stringPassed

    # We will be creating a Dictionary for the characters and would be storing the occurence of chars

    def reverseString(self):
        splitList = self.inputString.split(' ')

        for stringSection in splitList[::-1]:
            print stringSection,



if __name__ == "__main__":
    lenghtEncode = LengthEncoding("i love programming very much")
    lenghtEncode.reverseString()