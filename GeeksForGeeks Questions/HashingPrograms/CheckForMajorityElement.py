
class CheckMajority(object):

    def checkMajority(self,list):
        dictA = {}
        lenOfList = len(list)

        for element in list:
            if element in dictA:
                dictA[element] += 1
            else:
                dictA[element] = 1

        for key, value in dictA.items():
            if dictA[key] >= lenOfList / 2:
                assert isinstance(key, object)
                print "Majority Element found %d" % key


if __name__ == "__main__":
    majority = CheckMajority()
    majority.checkMajority([1, 1, 1, 2, 2, 2, 1, 2, 3, 1,2,1,1,1,2,2,4])
