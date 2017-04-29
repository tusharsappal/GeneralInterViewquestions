
# This program illustrates the concept of Caeser Cipher Algorithm

class CaeserCypher(object):

    def __init__(self,shift):
        self.shift = shift

    def encode(self,listChar):

        for index in range(0 , listChar.__len__()):
            listChar[index] =  unichr(ord(listChar[index])+self.shift)
        # We have our list ready , lets print the string generated out of this string
        print "Encoded String is %s " %("".join(listChar))

        # Now we will be calling the decoding method

        self.decode("".join(listChar))

    def decode(self, enocdedString):

        listChar = list(enocdedString)

        for index in range(0,listChar.__len__()):
            listChar[index] =  unichr(ord(listChar[index])-self.shift)

        print "Decoded and original string is %s" %("".join(listChar))


    def takeInput(self):
        string_input = raw_input("")
        # We will be converting the string into a list
        listChar = list(string_input)
        print "original string is %s" %(string_input)
        self.encode(listChar)


if __name__=="__main__":
    CaeserCypher(4).takeInput()