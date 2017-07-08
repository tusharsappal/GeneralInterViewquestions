'''
Write code to reverse a C-Style String. (C-String means that "abcd" is represented as five characters, including the null character.)
'''

class ReverseCStyleString(object):
    def __init__(self, stringToBeReversed):
        self.stringToreverse = stringToBeReversed


    def revereString(self):
        self.stringToreverse.__add__("\\")
        r = len(self.stringToreverse)-1

        for i in range(r , 0 , -1):
            print self.stringToreverse[i],




if __name__ == "__main__":
    reverse = ReverseCStyleString("Tushar")
    reverse.revereString()


