# This script checks for the array given to find the pair whose sum is equal to the one given

class CheckPairForSum(object):
    def checkPairForSum(self):
        print "Enter the Array , please note the numbers should be between 1 and 20 \n"
        string_input = raw_input()
        input_list = string_input.split()
        input_list = [int(a) for a in input_list]
        print "Array to be searched", input_list

        sum_entered = input("Enter the sum around which the pairs have to be searched")

        # We will initialize one array with 0 indexes

        bucket = [0]*50

        for index in range(0,input_list.__len__()-1):
            temp = sum_entered - input_list[index]
            if temp >=0 and bucket[temp] == 1:
                print "The sum is formed with the elements at position %d and %d" %(index+1, temp+1)

            bucket[input_list[index]] = 1


if __name__=="__main__":
    CheckPairForSum().checkPairForSum()
