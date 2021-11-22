from matplotlib import container
import numpy as np
from numpy.core.fromnumeric import partition
from numpy.random import default_rng
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from bubbleSort import bubbleSort
from quickSort import quickSort
from insertionSort import insertionSort
from selectionSort import selectionSort


# plt.style.use('dark_background')
# dark background breaks the whole program use safely

class TrackedArray():
    def __init__(self, arr):
        self.arr = np.copy(arr)
        self.reset()

    def reset(self):
        self.indices = []
        self.values = []
        self.access_type = []
        self.full_copies = []

    def track(self, key, access_type):
        self.indices.append(key)
        self.values.append(self.arr[key])
        self.access_type.append(access_type)
        self.full_copies.append(np.copy(self.arr))

    # to keep track of the activities
    # like which index was acessed or
    # what operation was performed
    # return type is either a list of tuples or a tuple
    def GetActivity(self, idx=None):
        if isinstance(idx, type(None)):
            return [(i, op) for (i, op) in zip(self.indices, self.access_type)]
        else:
            return (self.indices[idx], self.access_type[idx])

    def __getitem__(self, key):
        self.track(key, "get")
        return self.arr.__getitem__(key)

    def __setitem__(self, key, value):
        self.arr.__setitem__(key, value)
        self.track(key, "set")

    def __delitem__(self, key):
        self.track(key, "del")
        self.arr.__delitem__(key)

    def __len__(self):
        return self.arr.__len__()

    def __str__(self):
        return self.arr.__str__()

    def __repr__(self):
        return self.arr.__repr__()


FPS = 60.0

N = 50

# creating an array and rounding it off
arr = np.round(np.linspace(1, 1000, N), 0)
# if a pseudorandom number generator is reinitialized with the same seed,
# it will produce the same sequence of numbers.
# np.random.seed(0)

# shuffling the array
np.random.shuffle(arr)
print(arr)
arr = TrackedArray(arr)

print(arr)

fig, ax = plt.subplots(figsize=(16, 8))

fig.suptitle('Sorting Algorithms')
container = ax.bar(np.arange(0, len(arr), 1), arr, align='edge', width=0.8)
ax.set(xlabel="Index", ylabel="Value")
ax.set_xlim([0, N])

# function calls for the sorting algorithms
# uncomment as required

# bubbleSort(arr)
# insertionSort(arr)
# quickSort(arr, 0, len(arr)-1)

def update(frame):
    for (rectangle, height) in zip(container.patches, arr.full_copies[frame]):
        rectangle.set_height(height)
        rectangle.set_color('#1f77b4')

    return (*container,)


ani = animation.FuncAnimation(fig, update, frames=range(len(arr.full_copies)),
                              blit=True, interval=1000./FPS, repeat=False)

container = ax.bar(np.arange(0, len(arr), 1),
                   align="edge", width=0.8, height=arr)
plt.show()
