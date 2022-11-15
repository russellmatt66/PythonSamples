# Maximum Pairwise Product with np.outer
# Matt Russell
import numpy as np 
import sys # Command-line

def MaxPPy(numbers): # Wrapper
	result = 0
	num_array = np.outer(numbers,numbers)

	for i in np.arange(num_array.shape[0]):
		for j in np.arange(num_array.shape[1]):
			if i == j:
				num_array[i,j] = None # diagonal values don't matter
			elif num_array[i,j] > result:
				result = num_array[i,j]
	return result

n = int(sys.argv[1]) 
high = int(sys.argv[2])
result = 0

numbers = np.random.uniform(low = 0.0, high = high, size = n)
print("List of numbers is: ", numbers)

num_array = np.outer(numbers,numbers)

for i in np.arange(num_array.shape[0]):
	for j in np.arange(num_array.shape[1]):
		if i == j:
			num_array[i,j] = None # diagonal values don't matter
		elif num_array[i,j] > result:
			result = num_array[i,j]

print("Max PP is: ", result)

resultW = MaxPPy(numbers)
print("Max PP from wrapper is: ", resultW)

