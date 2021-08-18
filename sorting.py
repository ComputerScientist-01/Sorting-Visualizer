import numpy as np
from numpy.core.fromnumeric import partition
from numpy.random import default_rng
import scipy
import matplotlib.pyplot as plt
import matplotlib.animation as animation
# matplotlib.use('Agg')

N = 30

# creating an array and rounding it off
arr = np.round(np.linspace(1, 1000, N), 0)

# if a pseudorandom number generator is reinitialized with the same seed,
# it will produce the same sequence of numbers.
np.random.seed(0)

# shuffling the array
np.random.shuffle(arr)
print(arr)


fig, ax = plt.subplots(figsize=(16, 8))
fig.suptitle("Unsorted Array")
ax.set(xlabel="Index", ylabel="Value")
ax.set_xlim([0, N])
container = ax.bar(np.arange(0, len(arr), 1),
                   align="edge", width=0.8, height=arr)


# insertion sort
# sorter = "Insertion"
# for i in range(1, len(arr)):
#     key = arr[i]
#     j = i-1
#     while ((j >= 0) and (arr[j] > key)):
#         arr[j+1] = arr[j]
#         j -= 1
#     arr[j+1] = key

# print("\n after sorting: \n")
# print(arr)

# quick sort
sorter = "Quick"


def quicksort(arr, lo, hi):
    if(lo < hi):
        p = partition(arr, lo, hi)
        quicksort(arr, lo, p-1)
        quicksort(arr, p+1, hi)


def partition(arr, lo, hi):
    pivot = arr[hi]
    i = lo
    for j in range(lo, hi):
        if arr[j] < pivot:
            temp = arr[i]
            arr[i] = arr[j]
            arr[j] = temp
            i += 1
    temp = arr[i]
    arr[i] = arr[hi]
    arr[hi] = temp
    return i


quicksort(arr, 0, len(arr)-1)
print(arr)


fig, ax = plt.subplots(figsize=(16, 8))
fig.suptitle(f"{sorter} Sort")
ax.set(xlabel="Index", ylabel="Value")
ax.set_xlim([0, N])
container = ax.bar(np.arange(0, len(arr), 1),
                   align="edge", width=0.8, height=arr)
plt.show()
