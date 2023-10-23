# If Else in a List statement

# Example 1 - if statement before for loop (Ternary Expression)
def example1(nums = [1, 2, 3, 4]):
    selection = [i * 2 if i % 2 == 0 else i for i in nums]
    print(selection)

# Example 2 - if statement after for loop (Filtering Condition)
def example2(nums = [1, 2, 3, 4]):
    selection = [i * 2 for i in nums if i % 2 == 0]
    print(selection)

# Example 3 - Lambda in List Comprehension - using map
def example3(nums = [1, 2, 3, 4]):
    selection = list(map(lambda x: x * 5 if x > 2 else x, nums))
    print(selection)

# Example 4 - Lambda in List Comprehension - using filter
def example4(nums = [1, 2, 3, 4]):
    selection = list(filter(lambda x: x * 2 > 4, nums))
    print(selection)

# Example 5 - using Ternery and Filtering together
def example5(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]):
    selection = [i * 2 for i in nums if i > 5 in nums]
    print(selection)