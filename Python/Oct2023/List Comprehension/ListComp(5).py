# List Comprehension vs Reduce
from functools import reduce
from math import prod

# The reduce func repeats an action carries out a function to a sequence of iterables
# the function that is inside reduce needs to accept 2 parameters
# 1 is for the existing total, the 2nd is for the new item being processed

# For example, adding the values in a list together
def example1(nums=[1,2,3,4]):
    result = reduce(lambda x,y: x+y, nums)
    print(result)

# Reduce is seen as redundant and so a List Comprehension equivalent exists
# For Incrementation, the sum func can be used
def example2(nums=[1,2,3,4]):
    result = sum([i for i in nums])
    print(result)

# for multplication, different modules offer solutions with a prod function
def example3(nums=[1,2,3,4]):
    result = prod([i for i in nums])
    print(result)

# Flattening a list is turning a nested list into a 1D list
# We can do this by creating a For Loop inside a For Loop to represent the amount of dimensions
def example4(nums=[[1,2],[3,4],[5,6]]):
    result = [i for sublist  in nums for i in sublist]
    print(result)

# Reduce can do this by using the + operator to add lists together
def example5(nums=[[1,2],[3,4],[5,6]]):
    result = reduce(lambda x,y: x + y, nums)
    print(result)

# Reduce can display the highest value in a list
# List Comps cannot do this
def example6(nums=[1,2,3,4,5,6]):
    result = reduce(lambda x,y: x if x > y else y, nums)
    print(result)
