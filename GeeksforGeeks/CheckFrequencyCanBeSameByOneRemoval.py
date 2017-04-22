# This program check if frequency of all characters can become same by one removal

class CheckFrequencyCanBeSameByOneRemoval(object):
    def checkFrequcnyCanBeSame(self):
        input_string = raw_input("Enter the string to be checked")
        hashMap = [0]*128

        for character in input_string:
            hashMap[ord(character)] = hashMap[ord(character)]+1

        index = 0
        possible = False
        while index < hashMap.__len__()-1:
            if abs(hashMap[index-1]-hashMap[index]) ==1:
                possible = True
            index = index +1

        if possible is True:
            print "Yes"
        else:
            print "No"

if __name__=="__main__":
    CheckFrequencyCanBeSameByOneRemoval().checkFrequcnyCanBeSame()