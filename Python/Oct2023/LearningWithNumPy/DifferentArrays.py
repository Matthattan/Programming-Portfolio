import numpy as np

# Initializing Different Types of Array

# all 0s matrix
print(np.zeros(5))

# all 1s matrix
print(np.ones((4,2,2), dtype='int32'))
a = np.ones((4,2,2), dtype='int32')
# Any other number
print(np.full((2,2), 99))

# Create an array of a pre-existing shape
print(np.full_like(a, 3))

# Array of random (decimal) numbers
print(np.random.rand(4,2))

# Array of random (integer) numbers
print(np.random.randint(10, size=(3,3)))

# Getting identity matrix
print(np.identity(5))

# Repeat an array
arr = np.array([1,2,3])
r1 = np.repeat(arr, 3, axis=0)
print(r1)

# Challenge
result = np.full((5,5), 1)
z = np.zeros((3,3))
z[1,1] = 9
print(z)
result[1:4,1:4] = z
print(result)

# Copying array
c = np.array([1,2,3])
d = c.copy()
d[0] = 100
print(d)
print(c)