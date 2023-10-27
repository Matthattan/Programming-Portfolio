# 5 Ways to check if a list is empty

# An empty list is false when bool is used on it

# 1 - using implicit bool value of the list
def example1(List1=[], List2=["Hello", "World"]):
    if not List1:
        print("This List is Empty")
    else:
        print("This List is Full")

    
    if not List2:
        print("This List is Empty")
    else:
        print("This List is Full")

# 2 - Checks if the item is indeed a list AND empty
def example2(List1=[], List2=["Hello", "World"], Dict1={}, Dict2={"Hello":"World"}):
    if isinstance(List1, list) and not List1:
        print("This List is Empty")
    else:
        print("This List is Full")
    
    if isinstance(List2, list) and not List2:
        print("This List is Empty")
    else:
        print("This List is Full")

    if isinstance(Dict1, list) and not Dict1:
        print("This List is Empty")
    else:
        print("This List is Full")

    if isinstance(Dict2, list) and not Dict2:
        print("This List is Empty")
    else:
        print("This List is Full")

# 3 - using the any method
def example3(List1=[], List2=[[]], List3=["Hello", ["World"]]):
    if not any(List1):
        print("This List is Empty")
    else:
        print("This List is Full")
    
    if not any(List2):
        print("This List is Empty")
    else:
        print("This List is Full")

    if not any(List3):
        print("This List is Empty")
    else:
        print("This List is Full")

# 4 - Checking if the length of the list is equal to 0 using the len method
def example4(List1=[], List2=["Hello", "World"]):
    if len(List1) == 0:
        print("This List is Empty")
    else:
        print("This List is Full")
    
    if len(List2) == 0:
        print("This List is Empty")
    else:
        print("This List is Full")

# 5 - comparing list to an actual empty list
def example5(List1=[], List2=["Hello", "World"]):
    if List1 == []:
        print("This List is Empty")
    else:
        print("This List is Full")
    
    if List2 == []:
        print("This List is Empty")
    else:
        print("This List is Full")

# Solutions 1 and 2 are more efficient and python
# However Solutions 4 and 5 are readable and convenient