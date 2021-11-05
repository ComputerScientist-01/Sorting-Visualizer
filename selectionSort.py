# Selection sort in Python


def selectionSort(array):

    # keep track of swapping
    swapped = False

    # loop through each element of array
    for i in range(len(array)):

        # for keeping the smallest integer
        index = i

        # loop to compare array elements
        for j in range(i+1,len(array)):

            # change > to < to sort in descending order
            if array[j]<array[index]:

                # index is equal to the condition number
                index=j

                swapped=True

        # swapping occurs if elements
        # are not in the intended order

        temp=array[i]
        array[i]=array[index]
        array[index]=temp
       
        # no swapping means the array is already sorted
        # so no need for further comparison
        if not swapped:
            break

