# This program checks for the leader in the array
#An element is leader if it is greater than all the elements to its right side. And the rightmost element is always a leader.

class FindLeaderInArray(object):
    def findLeaderInArray(self):
        print "Enter the Array "
        string_input = raw_input()
        input_list = string_input.split()
        input_list = [int(a) for a in input_list]

        if input_list.__len__() == 1:
            print "Leader is %d " %(input_list[0])

        else:
            upper_limit = input_list.__len__()-1
            max = input_list[upper_limit]
            print max
            while (upper_limit >= 0):
                if input_list[upper_limit] > max:
                    print input_list[upper_limit]
                    max = input_list[upper_limit]
                upper_limit = upper_limit-1


if __name__=="__main__":
    FindLeaderInArray().findLeaderInArray()
