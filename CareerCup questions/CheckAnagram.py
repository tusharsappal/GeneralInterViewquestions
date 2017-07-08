'''
Write code to reverse a C-Style String. (C-String means that "abcd" is represented as five characters, including the null character.)
'''

class CheckAnagram(object):
    def __init__(self, firstString, secondString):
        self.firstString = firstString
        self.secondString = secondString

    def checkAnagram(self):
        tempArray = [0]*256

        for char in self.firstString:
            tempArray[ord(char)-1] = tempArray[ord(char)-1] + 1

        # Now subtracting the elements from second string and the above Temp Array

        for char in self.secondString:
            if tempArray[ord(char)-1] == 1:
                tempArray[ord(char)-1] = tempArray[ord(char)-1] - 1
            else:
                return False

        sum = 0
        for element in tempArray:
            sum = sum + element

        if sum == 0 :
            return True
        else:
            return False


if __name__ == "__main__":
    ana = CheckAnagram("abcd", "bac")
    if ana.checkAnagram():
        print "Strings are Anagrams"
    else:
        print "Strings are not Anangrams"


