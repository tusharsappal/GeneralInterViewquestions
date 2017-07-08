class IndexOfSortedArray(object):

    def findtheExtraElementIndex(self, list1, list2):

        lower = 0
        upper = len(list2) - 1
        index = 0

        while ( lower <= upper):
            mid = int ((lower + upper)/2)

            if list1[mid] == list2[mid]:
                lower = mid +1
            else:
                upper = mid -1
                index = mid


        print "The index which is Different between the two arrays is %d " %(index)



if __name__ == "__main__":
    list1 = [2, 4, 6, 8, 9, 10, 12]
    list2 = [2, 4, 6, 8, 10, 12]
    indexOfSorted = IndexOfSortedArray()
    indexOfSorted.findtheExtraElementIndex(list1, list2)
