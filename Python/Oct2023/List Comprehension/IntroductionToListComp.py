# Introduction to List Comprehension

# Example 1 - modifying values from array
def example1(nums = [1, 2, 3, 4]):
    result1 = [i * 2 for i in nums]
    print(result1)

# Example 2 - modifying strings
def example2(sentence = ["the", "glass", "prison"]):
    result2 = [i.upper() for i in sentence]
    print(result2)

# Example 3 - using functions inside lists
def example3(results = [], nums = [1, 2, 3, 4]):
    def double(i):
        return i * 2
    
    results = [double(x) for x in nums]
    print(results)

# Example 4 - if statements inside lists
def example4(results = [], nums = [1, 2, 3, 4]):
    results = [x * 2 for x in nums if x > 2]
    print(results)

# Example 5 - modifying list of dictionaries
def example5(results = [], dict = [{"name": "Matthattan"}, {"name": "Bob"}]):
    results = [i['name'] for i in dict]
    print(results)
