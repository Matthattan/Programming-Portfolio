# Map Built-In Function

# Map requires a function to run and the list to iterate through
# Map executes the function for every item in the list

def example1(nums = [1, 2, 3, 4]):
    result = list(map(lambda x: x * 2, nums))
    print(result)

# Connecting Filter with Map Function
# Filter takes items from the list that meets the condition inside the function

def example2(nums = [1, 2, 3, 4]):
    result = list(filter(lambda x: x > 4, map(lambda x: x * 2, nums)))
    print(result)

# Using a function rather than lambda is more time efficient
def example3(nums = [1, 2, 3, 4]):
    def timesTwo(x):
        return x*2
    
    result = list(map(timesTwo, nums))
    print(result)

# However, not using a map results in a lambda being faster
def example4(nums = [1, 2, 3, 4]):
    result = [x * 2 for x in nums]
    print(result)

# Lambdas become more time efficient as more items are added
# Try not to use Lambda with Map, try using lambdas in conjunction with list comprehension for efficiency