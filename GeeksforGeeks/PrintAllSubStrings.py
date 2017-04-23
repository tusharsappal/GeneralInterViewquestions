# This Program prints all the substring of a string

class PrintAllSubStrings(object):
    def printallSubStrings(self):
        string_input =  raw_input("Enter the String")
        len_of_string = string_input.__len__()

        count = 0
        for indexi in range(0, len_of_string):
            for indexj in range(indexi, len_of_string):
                print string_input[indexi:indexj+1]
                count = count +1


        print "Count is %d " %(count)

if __name__=="__main__":
    PrintAllSubStrings().printallSubStrings()

