import numpy as np
# Accessing/Changing Elements, Row, Columns etc

a = np.array([[1,2,3,4],[5,6,7,8]])

# Getting a specific element
# Get 7
print(a[1,2])

# Get a specific row
# Get first row
print(a[0, :])

# Get a specific column
# Get second column
print(a[:, 1])

# Getting elements that fit a pattern
# Get every other number from row 1
print(a[0, 1:4:2])

# Change an element
# Change 7 to 10
a[1,2] = 10
print(a)

# Getting element of a multi-dimensional array (outside in)
# Get 6
b = np.array([[[1,2],[3,4]],[[5,6],[7,8]]])
print(b[1,0,1])

# Replacing an array inside a multi-dimensional array
b[1,:] = [[9, 10],[11, 12]]
print(b)