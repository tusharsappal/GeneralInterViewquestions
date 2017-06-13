
def subSetSums(listOfElements, l , r , sum=0):

    if l > r:
        print sum
        return
    # Including listOfElements[l]
    subSetSums(listOfElements , l+1, r , sum+listOfElements[l])

    # Excluding listOfElements[l]
    subSetSums(listOfElements, l+1, r, sum)



listOfElements = [5, 4, 3]
subSetSums(listOfElements, 0 , len(listOfElements)-1 , 0)