
# This program prints the pairs with the same sum 

class PairWithSameProduct(object):
    def pairWithSameProduct(self):
        string_input = raw_input()
        input_list = string_input.split(',')
        input_list = [int(a) for a in input_list]

        dict= {}

        for index in range(0,input_list.__len__()-1):
            for indexj in range(index+1,input_list.__len__()-1):
                product = input_list[index] * input_list[indexj+1]
                if product in dict:
                    print "Elements are present at index %d , %d , %d , %d" %(index, indexj+1, dict[product][0], dict[product][1])
                else :
                    tempList = [index, indexj+1]
                    dict[product] = tempList


if __name__=="__main__":
    PairWithSameProduct().pairWithSameProduct()