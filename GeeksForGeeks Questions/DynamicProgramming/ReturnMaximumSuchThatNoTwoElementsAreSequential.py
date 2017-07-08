
def returnMaxSumNotAdjcent(arr):

    incl = 0
    excl = 0

    for i in arr:
        new_excel = excl if excl > incl else incl

        incl = excl + i
        excl = new_excel

    return excl if excl > incl else incl


arr = [5, 5, 10, 100, 10, 5]
print "The maximum sum is %d " %returnMaxSumNotAdjcent(arr)
