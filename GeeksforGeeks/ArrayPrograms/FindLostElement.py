# Find the lost element from array

class FindMissingElemet(object):
    def findmissingElementFromTwoArrays(self):
        print "Enter the first Array "
        string_input = raw_input()
        input_list_1 = string_input.split()
        input_list_1 = [int(a) for a in input_list_1]

        print "Enter the Second Array "
        string_input_2 = raw_input()
        input_list_2 = string_input_2.split()
        input_list_2 = [int(a) for a in input_list_2]

        # We will find summation of both the arrays and the difference between the sum of the arrays would give us the
        # missing number

        sum_1=0
        sum_2=0

        for index in range(0, input_list_1.__len__()):
            sum_1 = sum_1 + input_list_1[index]

        for index in range(0, input_list_2.__len__()):
            sum_2 = sum_2+ input_list_2[index]

        print "The Missing number is %d" %abs((sum_1-sum_2))


if __name__=="__main__":
    FindMissingElemet().findmissingElementFromTwoArrays()