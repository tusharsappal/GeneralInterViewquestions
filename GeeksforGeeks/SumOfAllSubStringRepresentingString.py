'''This program prints Sum of all substrings of a string representing a number
We will be using the Concept of Dynamic Programing
We can solve this problem using dynamic programming. We can write summation of all substrings on basis of digit at which they are ending in that case,
Sum of all substrings = sumofdigit[0] + sumofdigit[1] + sumofdigit[2] and so on + sumofdigit[n-1] where n is length of string.

Where sumofdigit[i] stores sum of all substring ending at ith index digit, in above example,

Example : num = "1234"
sumofdigit[0] = 1 = 1
sumofdigit[1] = 2 + 12  = 14
sumofdigit[2] = 3 + 23  + 123 = 149
sumofdigit[3] = 4 + 34  + 234 + 1234  = 1506
Result = 1670

General Logic = sum[i] = (i+1)*array[i]+ '''


class SumOfAllSubStringsRepresentingString(object):



    def printSumOfSubString(self):

        string_input = raw_input("Enter the String")
        len_of_string = string_input.__len__()

        sum_of_digit = [0]*len_of_string
        sum_of_digit[0] = int(string_input[0])
        res= sum_of_digit[0]

        index = 0

        for index in range(1 , len_of_string):
            numi = int(string_input[index])

            sum_of_digit[index] = (index+1)*numi+ 10* sum_of_digit[index-1]

            res = res+ sum_of_digit[index]

        print res

if __name__=="__main__":
    SumOfAllSubStringsRepresentingString().printSumOfSubString()