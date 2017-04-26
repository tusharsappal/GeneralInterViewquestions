# This code finds the local minima in an array
'''
Given an array arr[0 .. n-1] of distinct integers, the task is to find a local minima in it. We say that an element arr[x] is a local minimum if it is less than or equal to both its neighbors.

For corner elements, we need to consider only one neighbor for comparison.
There can be more than one local minima in an array, we need to find any one of them.

'''


class LocalMinima(object):

    def findLocalMin(self, input_list, startIndex, EndIndex, length):
        mid = int (startIndex+(startIndex+ EndIndex/2))

        if (mid is 0 or input_list[mid-1]> input_list[mid] and mid == length-1 or input_list[mid] < input_list[mid+1]):
            return  mid
        # if the middle element is not minima and its left
        # neighbour is smaller than it , thn left half must have a local minima

        elif mid > 0 and input_list[mid-1] < input_list[mid]:
            return self.findLocalMin(input_list, startIndex, mid - 1, length)

        return self.findLocalMin(input_list,mid+1,EndIndex,length)

    def localMinima(self):
        string_input = raw_input()
        input_list = string_input.split(',')
        input_list = [int(a) for a in input_list]

        print "local minima is present at index %d" %(self.findLocalMin(input_list, 0 , len(input_list)-1, len(input_list)))




if __name__=="__main__":
    LocalMinima().localMinima()