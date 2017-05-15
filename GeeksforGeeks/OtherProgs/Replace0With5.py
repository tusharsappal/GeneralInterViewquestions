class Replace0With5(object):

    def _replace(self, number):

        tempNumber = 0
        index = 0
        while number > 0:
            remainder = number % 10
            if remainder == 0:
                remainder = 5

            tempNumber = tempNumber + (10**index) * remainder
            index = index+1
            number = number /10

        print "Replaced Number is %d" %(tempNumber)


    def replace(self, number):
        if number == 0:
            return  5
        else:
            self._replace(number)



if __name__ == "__main__":
    inputNumber = raw_input("Enter the number to be changed")
    inputNumber = int(inputNumber)
    replace = Replace0With5()
    replace.replace(inputNumber)
