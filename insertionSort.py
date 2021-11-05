# Insertion sort in Python
def insertionSort(array):

    # keep track of swapping
    
    # loop through each element of array
    for i in range(1,len(array)):

        # Setting the desired key element
        key=array[i]
        j=i-1

        # Swapping the key and compared number 
        # swapping occurs if elements
        # are not in the intended order 
        while((j>-1) and (array[j]>key)):
            array[j+1]=array[j]
            j=j-1
        
        array[j+1]=key
    