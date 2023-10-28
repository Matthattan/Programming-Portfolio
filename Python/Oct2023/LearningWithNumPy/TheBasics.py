import numpy as np

# The Basics

# Initialising and Printing an array with NumPy
a = np.array([1,2,3])
print(a)

# Initialising a 2D Array and Printing a 2D Array with NumPy
b = np.array([[1, 2],[3, 4]])
print(b)

# Getting Dimension
print(a.ndim)

# Getting Shape
print(b.shape)

# Getting Type
print(a.dtype)

# Getting Size
print(a.itemsize)