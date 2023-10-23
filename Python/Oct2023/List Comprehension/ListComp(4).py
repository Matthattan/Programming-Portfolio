# List Comprehension vs Filter function

# Filter function expects a function and an iterable to run through
# The function should check a condition for all items passed through
def example1(nums=[1,2,3,4]):
    def grTwo(i):
        return i>2
    
    result = list(filter(grTwo, nums))
    print(result)

    # List Comp equivalent
    result = [i for i in nums if grTwo(i)]
    print(result)

# using a Lambda with filter
def example2(nums=[1, 2, 3, 4]):
    result = list(filter(lambda x: x > 2, nums))
    print(result)

# putting None as the first argument in a filter func prevents anything false-y from being returned
def example3(nums=[0, 0, 1, 2, True, False]):
    result = list(filter(None, nums))
    #prints only [1, 2, True]
    print(result)

# Using a function in a list comp is faster than a lambda or function in a filter func but an if statement in a list comp is overall faster

