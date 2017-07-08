
class Anagram(object):

    def __init__(self, string1, string2):
        self.string1 = string1
        self.string2 = string2

    # We will be creating a Dictionary for the characters and would be storing the occurence of chars

    def checkAnagram(self):

        dict1 = {}

        for character in self.string1:

            if character in dict1:
                dict1[character] = dict1[character] + 1
            else:
                dict1[character] = 1

        # Now we have the elements fitted into it dictionary we would be traversing the dictionary and if the
        # character of second string is present we would be removing it from the dictionary , if all the elements in the
        # dictionary are zero then we have an anagram

        for character in self.string2:
            if character in dict1:
                dict1[character] = dict1[character] - 1
                if dict1[character] == 0 :
                    del dict1[character]

        if dict1:
            print "Strings are not Anagram"
        else:
            print "Strings are anagram"


if __name__ == "__main__":
    anagram = Anagram("listen", "silent")

    anagram.checkAnagram()