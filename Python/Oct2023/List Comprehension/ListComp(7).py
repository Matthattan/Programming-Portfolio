# List Comp with multiple FOR Loops

# The left-most FOR loop is the outer for loop while the loops going to the right are nested 
def example1(nums=[1,2,3,4], letters=["a","b","c","d"]):
    combination = [(n, l) for n in nums for l in letters]
    print(combination)

# You can flatten nested lists using double FOR loops
# You can use as many FOR loops as needed for the amount of nested Lists
def example2(nestedList=[[1,2],[3,4],[5,6]]):
    flattenList = [item for childList in nestedList for item in childList]
    print(flattenList)

# You can insert list data into different data structures
def example3(nums=[1,2,3,4], 
             letters=["a","b","c","d"]):
    result = [{k:v} for k in nums for v in letters]
    # produces a dictionary 
    print(result)

# Working with lists of different lengths/amounts results in the product being relative to the list of the lowest amount
# This works no matter the order of FOR loops/whichever list is smaller
def example4(nums=[1,2, 3, 4], 
             letters=["a","b","c",]):
    result = [{k:v} for k in nums for v in letters]
    # produces a dictionary 
    print(result)

# Unused values are possible in List Comp but can be seen as unnecessary
def example5(nums=[1,2,3,4], 
             letters=["a","b","c","d"]):
    # You can use an underscore for unused values
    result = [(k) for k in nums for _ in letters]
    # produces a dictionary 
    print(result)

example5()

    