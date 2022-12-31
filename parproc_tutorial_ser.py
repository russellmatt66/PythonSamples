# From here: https://www.machinelearningplus.com/python/parallel-processing-python/
# Serial solution
# Optional Exercise from: https://www.coursera.org/learn/introduction-to-concurrent-programming/supplement/z4MFx/optional-python-parallel-programming-resources

import numpy as np
from time import time

def how_many_within_range(row,l,h):
    # row - from matrix
    # l - low 
    # h - high
    # l < h
    # 0 <= l < 10
    # 0 < h <= 10
    # Magic numbers from program bulk
    howmany = 0
    for n in row:
        if (n >= l and n <= h):
            howmany += 1
    return howmany

# Prepare data
np.random.RandomState(100)
arr = np.random.randint(0,10, size=[200000, 5])
data = arr.tolist()
# data[:5] - first five rows

results = []
for row in arr:
    results.append(how_many_within_range(row, l = 4, h = 8))

print(results[:10])