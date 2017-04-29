# A simple class demonstrating Binary Search
class BinarySearch(object):
    def binarySearch(self):
        print "Enter the Sorted Array \n"
        string_input = raw_input()
        input_list = string_input.split()
        input_list = [int(a) for a in input_list]
        print "Array to be searched", input_list

        # Binary Search Logic starts here
        num_to_be_searched = int(input("Enter number to be searched"))

        lower_limit = 0
        higher_limit = input_list.__len__()-1
        middle = (lower_limit+higher_limit) / 2

        while ( lower_limit <= higher_limit):
            if num_to_be_searched == input_list[middle]:
                print "Number found at %d" %(middle+1)
                break
            if input_list[middle] < num_to_be_searched:
                lower_limit = middle +1
            else :
                higher_limit = middle -1
            middle = (higher_limit+lower_limit)/2


        if ( lower_limit > higher_limit):
            print "Number not found"


if __name__ == '__main__':
    BinarySearch().binarySearch()
