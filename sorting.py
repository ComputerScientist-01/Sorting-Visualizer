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
