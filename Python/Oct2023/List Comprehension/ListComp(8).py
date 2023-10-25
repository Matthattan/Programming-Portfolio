# 3 Ways to print list comprehensions

# Using Print inside a list comp
def example1(nums=[1,2,3,4]):
    result = [print(i) for i in nums]
    #None for each value in nums
    print(result)

# Using print outside the list comp
def example2(nums=[1,2,3,4]):
    print([i for i in nums])

# using print inside list comp and OR
def example3(nums=[1,2,3,4]):
    result = [print(i) or i for i in nums]
    #i for each value in nums
    print(result)