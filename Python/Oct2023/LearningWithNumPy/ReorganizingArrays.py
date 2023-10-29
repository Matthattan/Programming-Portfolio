import numpy as np

# Reshaping arrays
array1a = np.array([[3,2,4,1],[7,6,8,5]])
array1b = array1a.reshape((8,1))
print(array1b)
array1c = array1b.reshape((2,2,2))
print(array1c)

# Reshaping does not work when converting into a shape that cannot fit all elements flush

# Vertically stacking vectors
array2a = np.array([1,2,3,4])
array2b = np.array([5,6,7,8])
array2c = np.vstack([array2a, array2b])
print(array2c)

# Horizontally stacked vectors
array3a = np.array([[1,2],[3,4]])
array3b = np.array([[5,6],[7,8]])
array3c = np.hstack([array3a, array3b])
print(array3c)