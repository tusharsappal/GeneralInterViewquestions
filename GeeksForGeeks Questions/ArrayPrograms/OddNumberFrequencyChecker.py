# This script checks if we have odd number of occurrences of a number

class OddNumberOfOccurences(object):
    def oddNumberChcker(self):
        print "Enter the Array , please note the numbers should be between 1 and 20 \n"
        string_input = raw_input()
        input_list = string_input.split()
        input_list = [int(a) for a in input_list]
        print "Array to be searched", input_list

        temp = 0
        for index in range(0, input_list.__len__()):
            # != is XOR in python
            temp = temp ^ input_list[index]

        print "The number having odd number of occurrences is %d" %(temp)


if __name__=="__main__":
    OddNumberOfOccurences().oddNumberChcker()
