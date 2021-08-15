import numpy as np
import scipy
import matplotlib.pyplot as plt
import matplotlib.animation as animation

N = 30

# creating an array and rounding it off
arr = np.round(np.linspace(1, 1000, N), 0)

# shuffling the array
np.random.shuffle(arr)
print(arr)


# insertion sort

for i in range(1, len(arr)):
    key = arr[i]
    j = i-1
    while ((j >= 0) and (arr[j] > key)):
        arr[j+1] = arr[j]
        j -= 1
    arr[j+1] = key

print("\n after sorting: \n")
print(arr)
