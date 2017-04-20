import math


class JumpSearch(object):
    def jumpSearch(self):
        print "Enter the Sorted Array \n"
        string_input = raw_input()
        input_list = string_input.split()
        input_list = [int(a) for a in input_list]
        print "Array to be searched", input_list

        num_to_be_searched = int(input("Enter number to be searched"))

        array_size = input_list.__len__()
        block_size = int(math.floor(math.sqrt(array_size)))
        i = 1
        start = 0

        while (input_list[i * (block_size - 1)] < num_to_be_searched):
            start = (i - 1) * block_size
            i = i + 1

        # Now we will be performing the linear search from the start to start+ block_size

        not_found = 1

        for index in range(start, start + block_size):
            if input_list[index] == num_to_be_searched:
                print "Number found at index %d" % (index + 1)
                not_found = 0
                break

        if not_found == 1:
            print "Number not found in the list"


if __name__ == '__main__':
    JumpSearch().jumpSearch()
