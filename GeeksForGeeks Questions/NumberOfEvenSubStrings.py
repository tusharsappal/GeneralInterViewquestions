# The following program prints the number of even substrings  in a string of digits

class EvenSubstring(object):
    def numberOfEvenSubString(self):
        print "Enter the Sting \n"
        string_input = raw_input()
        count = 0

        for index in range(0,string_input.__len__()):
            temp = int(string_input[index]-'0')

            if (temp%2 ==0):
                count = count+(index+1)

        print "count is %d" %(count)



if __name__=="__main__":
    EvenSubstring().numberOfEvenSubString()


