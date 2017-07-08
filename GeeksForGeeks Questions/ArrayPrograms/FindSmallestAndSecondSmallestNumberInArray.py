
class SmallandSecondSmall(object):

    def findValues(self, list):
        smallest = list[0]
        secondSmall = list[0]

        for index in range(0, len(list)):
            if list[index] < smallest:
                smallest = list[index]
            if list[index] > smallest and list[index] < secondSmall:
                secondSmall = list[index]


        print "Smallest element is %d" %(smallest)
        print "Second Smalles Element is %d" %(secondSmall)



if __name__ == "__main__":
    small = SmallandSecondSmall()
    small.findValues([12,13,1,10,34,1])
    small.findValues([12, 13, 12, 13, 34, 1])
