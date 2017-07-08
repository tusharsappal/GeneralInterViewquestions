
class SumOfNonRepeatingElements(object):


    def doSum(self):
        self.list = [1, 10, 9, 4, 2, 10, 10, 45 , 4]
        countDict = {}

        for item in self.list:
            if item in countDict:
                continue
            else:
                countDict[item] = 1

        sum = 0


        for key , value in countDict.items():
            if countDict[key] == 1:
                sum += key

        print "Sum is %d" %(sum)

if __name__ == "__main__":

    sumNonRepeating = SumOfNonRepeatingElements()
    sumNonRepeating.doSum()