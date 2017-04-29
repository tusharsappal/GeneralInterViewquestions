# This script does the exponential search
# First finds the probable range in which the number will fall into
# Once the range is decided we run the Binary Search on it
# The array should be sorted
class ExponentialSearch(object):
    def exponentialSearch(self):
        print "Enter the Sorted Array \n"
        string_input = raw_input()
        input_list = string_input.split()
        input_list = [int(a) for a in input_list]
        print "Array to be searched", input_list

        num_to_be_searched = int(input("Enter number to be searched"))
        length_of_array =input_list.__len__()-1

        if (input_list[0] == num_to_be_searched):
            print "Number found at position 1"
        else:
            i =1
            while i<length_of_array and input_list[i] <= num_to_be_searched :
                i = i *2

            # Now we will be performing the Binary Search on it

            lower_limit = 0
            higher_limit = i
            middle = (lower_limit + higher_limit) / 2
            while (lower_limit <= higher_limit):
                if num_to_be_searched == input_list[middle]:
                    print "Number found at position %d" % (middle + 1)
                    break
                if input_list[middle] < num_to_be_searched:
                    lower_limit = middle + 1
                else:
                    higher_limit = middle - 1
                middle = (higher_limit + lower_limit) / 2

            if (lower_limit > higher_limit):
                print "Number not found"


if __name__=="__main__":
    ExponentialSearch().exponentialSearch()