# Count substrings with same first and last characters
# First We will find the substrings from the string
# Then we will check if the substring has the property if the first and the last character is same , this is true for
# the single character

class PrintAllSubStrings(object):
    def printallSubStrings(self):
        string_input =  raw_input("Enter the String")
        len_of_string = string_input.__len__()

        count = 0
        for indexi in range(0, len_of_string):
            for indexj in range(indexi, len_of_string):
                temp_string =string_input[indexi:indexj+1]
                if temp_string[0] is temp_string[temp_string.__len__()-1]:
                    count = count+1

        print "Count is %d " %(count)

if __name__=="__main__":
    PrintAllSubStrings().printallSubStrings()

