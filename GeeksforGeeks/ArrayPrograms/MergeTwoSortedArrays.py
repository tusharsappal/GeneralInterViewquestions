# This script merges two sorted array

class MergeSortedArrays(object):

    def mergeSortedArray(self, list1, list2):

        lenOfResult = len(list1) + len(list2)

        list3 = [0]* (lenOfResult)
        len1 = len(list1)
        len2 = len(list2)

        iterator1 = 0
        iterator2 = 0
        resultantIterator = 0

        while iterator1 < len1 and iterator2 < len2:
            if list1[iterator1]< list2[iterator2]:
                list3[resultantIterator] = list1[iterator1]
                iterator1 = iterator1 + 1
                resultantIterator = resultantIterator + 1
            elif list2[iterator2] < list1[iterator1]:
                list3[resultantIterator] = list2[iterator2]
                iterator2 = iterator2 + 1
                resultantIterator = resultantIterator + 1
            else:
                list3[resultantIterator] = list1[iterator1]
                iterator1 = iterator1 +1
                resultantIterator = resultantIterator + 1
                list3[resultantIterator] = list2[iterator2]
                iterator2 = iterator2 +1
                resultantIterator = resultantIterator + 1



        # Now filling up the remaining elements if remaining from any array element

        while iterator1 <= len(list1)-1:
            list3[resultantIterator] = list1[iterator1]
            resultantIterator = resultantIterator +1
            iterator1 = iterator1 +1

        while iterator2 < len(list2) -1:
            list3[resultantIterator] = list2[iterator2]
            resultantIterator = resultantIterator +1
            iterator2 = iterator2 +1


        print list3[::]




if __name__ == "__main__":
    list1 = [ 5, 8, 9]
    list2 = [4, 7, 8]
    mergeSorted = MergeSortedArrays()
    mergeSorted.mergeSortedArray(list1, list2)