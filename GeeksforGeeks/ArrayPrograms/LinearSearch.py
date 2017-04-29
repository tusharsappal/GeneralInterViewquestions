# A simple class demonstrating Linear Search
class Example(object):
    def linearSearch(self):
        string_input = raw_input()
        input_list = string_input.split()
        input_list = [int(a) for a in input_list]
        print "Array to be searched" , input_list

        num_to_be_searched = int (input("Enter number to be searched"))
        index = 1
        for num in input_list:
            if num_to_be_searched == num:
                print "Number found at index %d" % (index)
                break
            index= index+1

if __name__ == '__main__':
    Example().linearSearch()

