# We will be using the hashing technique here
# We will store the chanracters ASCII 0 to 127 in a HASH , populate the hash and see which value is greatest


class ReturnHighestNumberOfCharacters(object):
    def returnHighestNumberOfChars(self):
        string_input = raw_input()

        # Declaring the Has Array

        hashArray = [0]*128
        for character in string_input:
            index = ord(character)
            hashArray[index] = hashArray[index] +1

        max = 0


        for character in string_input:
            if hashArray[ord(character)] > max:
                max = hashArray[ord(character)]
                charMax = character

        print "The maximum occurring character is %c" %(charMax)


if __name__=="__main__":
    ReturnHighestNumberOfCharacters().returnHighestNumberOfChars()