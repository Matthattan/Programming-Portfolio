# Unused variables in List Comp

# Using a self-explanatory variable name to show obsoleteness

def example1():
    result = ["Hello" for unusedVar in range(10)]
    print(result)

# Using an underscore ( _ ) to prevent python warning
def example2():
    result = ["Hello" for _ in range(10)]
    print(result)

# Using an underscore for multiple variables/key-value pairs
def example3(genericDict = {"1":"A","2":"B","3":"C"}):
    result = [value for _,value in genericDict.items()]
    print(result)

example3()