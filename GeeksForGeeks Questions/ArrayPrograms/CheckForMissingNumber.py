# This script checks for the missing number in the array
# If the array has 1 to n numbers in a ny order ( with one number in between missing ) , we will run n*(n+1)/2

class CheckForMissingNumber(object):
    def checkForMissingNumber(self):
        print "Enter the Array , skip any number \n"
        string_input = raw_input()
        input_list = string_input.split()
        input_list = [int(a) for a in input_list]
        print "Array to be searched", input_list

        len_of_array= input_list.__len__()
        sum = len_of_array*(len_of_array+1)/2

        for index in range(0,len_of_array):
            sum = abs(sum - input_list[index])

        print "The number missing is %d" %(sum)

if __name__=="__main__":
    CheckForMissingNumber().checkForMissingNumber()