# A simple class demonstrating merge Sort
class MergeSort(object):
    def _merge(self, list , loweLimit, mid, upperLimit):
        n1 = mid -loweLimit +1
        n2 = upperLimit -mid
        L = [0] * (n1)
        R = [0] * (n2)
        # Copy data to temp arrays L[] and R[]
        for i in range(0, n1):
            L[i] = list[loweLimit + i]

        for j in range(0, n2):
            R[j] = list[mid + 1 + j]

        # Merge the temp arrays back into arr[l..r]
        i = 0  # Initial index of first subarray
        j = 0  # Initial index of second subarray
        k = loweLimit  # Initial index of merged subarray

        while i < n1 and j < n2:
            if L[i] <= R[j]:
                list[k] = L[i]
                i += 1
            else:
                list[k] = R[j]
                j += 1
            k += 1

        # Copying the remaining items in sorted order in the Original Array

        while i < n1:
            list[k] = L[i]
            i += 1
            k += 1

        while j< n2:
            list[k] = R[j]
            k += 1
            j += 1


    def _mergeort(self, list , loweLimit, UpperLimit):
        if loweLimit < UpperLimit:
            mid = int((loweLimit+UpperLimit)/2)

            self._mergeort(list,loweLimit, mid)
            self._mergeort(list,mid+1, UpperLimit)
            self._merge(list,loweLimit, mid, UpperLimit)


    def mergeSort(self):
        print "Enter the  Array \n"
        string_input = raw_input()
        input_list = string_input.split()
        input_list = [int(a) for a in input_list]
        print "Array to be Sorted", input_list

        self._mergeort(input_list, 0, len(input_list)-1)

        print "Sorted array is \t",
        for element in input_list:
            print element


if __name__ == '__main__':
    MergeSort().mergeSort()