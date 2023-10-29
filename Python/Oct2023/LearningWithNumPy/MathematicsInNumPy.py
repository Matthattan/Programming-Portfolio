import numpy as np
# Mathematics

# Arithmetic with elements inside arrays
# Changing all values by a set value
a = np.array([1,2,3,4])
print(a + 2)
print(a - 2)
print(a*a)

# Adding with other arrays
b = np.array([5,6,7,8])
print(a + b)

# Linear Algebra

# 
c = np.ones((3,2))
d = np.full((2,3), 2)

print(c)
print(d)
e = np.matmul(c,d)
print(e)

# Finding deteminant
print(np.linalg.det(np.identity(3)))

# Statistics
f = np.array([1,3,2,2])
print(np.min(f, axis=0))
print(np.max(f))
print(np.sum(f))
