
# This script prints the Recman's sequence


class Recman(object):

    def rec(self, list,x):
        if x is 1:
            list.append(x)
            return x
        else:
            a = self.rec(list,x-1)
            am = a-x
            ap = a+x
            if am > 0 and am not in list:
                list.append(am)
                return am
            else:
                list.append(ap)
                return  ap


    def printRecman(self):
        string_input = raw_input("Enter the range")
        int_input = int(string_input)
        list = []
        self.rec(list,int_input)

        for element in list :
            print element

        # We will create an empty dictionary and will psuh the elements computed


if __name__=="__main__":
    Recman().printRecman()