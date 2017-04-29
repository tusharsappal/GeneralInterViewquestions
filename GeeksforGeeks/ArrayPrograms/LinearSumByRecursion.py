# This script prints the linear sum

class LinearSumByRecursion(object):

    def doSum(self,index, input_list):
        sum = 0
        if index < 0:
            return 0
        else :
            sum = input_list[index-1] + self.doSum(index-1, input_list)
            return sum

    def linearSum(self):
        string_input = raw_input()
        input_list = string_input.split(',')
        input_list = [int(a) for a in input_list]
        print "The Sum is %d " %(self.doSum(len(input_list)-1, input_list))


if __name__=="__main__":
    LinearSumByRecursion().linearSum()