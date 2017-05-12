
class SortZeroesOnesTwos(object):


    def SortNumerals(self):
        self.list = [0, 1, 1, 0, 1, 2, 1, 2, 0, 0, 0, 1]
        countDict = {}

        for item in self.list:
            if item in countDict:
                countDict[item] = countDict[item] + 1
            else:
                countDict[item] = 1

        newArray = [0] * len(self.list)

        index = 0

        for key , value in countDict.items():
            count = 0
            while count != value:
                newArray[index] = key
                index = index +1
                count = count +1

        print newArray[::]


if __name__ == "__main__":

    sort = SortZeroesOnesTwos()
    sort.SortNumerals()