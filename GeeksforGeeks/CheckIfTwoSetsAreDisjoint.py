# This script checks if the two sets are disjoint or not
'''

Input: set1[] = {12, 34, 11, 9, 3}
       set2[] = {2, 1, 3, 5}
Output: Not Disjoint
3 is common in two sets.

'''


class DisjoinChecker(object):
    def disjointChecker(self):
        string_input = raw_input("Enter first set")
        input_list_1 = string_input.split(',')
        input_list_1 = [int(a) for a in input_list_1]

        string_input_2 = raw_input("Enter the second set")
        input_list_2 = string_input_2.split(',')
        input_list_2 = [int(a) for a in input_list_2]

        # checking the length of the both the list
        len_1 = len(input_list_1)
        len_2  = len(input_list_2)
        dictA = {}
        dictB = {}

        # We will be populating the dictionary with the input arrays

        for index in range(0,input_list_1.__len__()):
            dictA[index] = input_list_1[index]

        for index in range(0,input_list_2.__len__()):
            dictB[index]  = input_list_2[index]

        if len_1 < len_2:
            smallArray = 1
        elif len_2 < len_1:
            smallArray = 2

        disjoint = 1

        if smallArray is 1 :

            for key, value in dictA.items():
                if value in dictB.values():
                    disjoint = 0
        if smallArray is 2:

            for key ,value in dictB.items():
                if value in dictA.values():
                    disjoint = 0

        if disjoint is 0:
            print "The two sets are not disjoint"
        else :
            print "The two sets are disjoint"




if __name__=="__main__":
    DisjoinChecker().disjointChecker()
