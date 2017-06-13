# Given an almost sorted array where only two elements are swapped, how to sort the array efficiently?
#
# Example
#
# Input:  arr[] = {10, 20, 60, 40, 50, 30}
# // 30 and 60 are swapped
# Output: arr[] = {10, 20, 30, 40, 50, 60}
#
# Input:  arr[] = {10, 20, 40, 30, 50, 60}
# // 30 and 40 are swapped
# Output: arr[] = {10, 20, 30, 40, 50, 60}
#
# Input:   arr[] = {1, 5, 3}
# // 3 and 5 are swapped
# Output:  arr[] = {1, 3, 5}

class SortAlmostSorted(object):

    def sortAlmostSortedArray(self,list1):

        # We would be starting from right most element to find the culprit element , once we have that
        # We will be traversing from the left most element to find the another culprit element
        # Once we have both , we will swap them .
        culpritIndex1 = 0
        culpritIndex2 = 0

        for index in range( len(list1)-1 ,1 , -1):
            if list1[index] < list1[index-1]:
                culpritIndex1 = index
                break


        for index in range(0 , len(list1)-1):
            if list1[index] > list1[culpritIndex1]:
                culpritIndex2 = index
                break

        # Now we have two culprit Indexes , we will be swapping them

        temp = list1[culpritIndex1]
        list1[culpritIndex1] = list1[culpritIndex2]
        list1[culpritIndex2] = temp


        # Now we will print the array

        print list1[::]


if __name__ == "__main__":
    list1 = [10, 20, 40, 30, 50, 60]
    sortAlmostSorted = SortAlmostSorted()
    sortAlmostSorted.sortAlmostSortedArray(list1)