# Exception Handling in List Comp

# You cannot handle exceptions (with try except) in one line

# Example 1 - List Comp inside of Try Except
def example1(nums=[0,1,2,3,4]):
    try:
        result = [1/num for num in nums]
    except ZeroDivisionError:
        print(ZeroDivisionError)
        result = ["Oops"]
        print(result)

# Example 2 - customised function with lambda
def catch(func, handle=lambda e: e, *args, **kwargs):
    try:
        return func(*args, **kwargs)
    except Exception as e:
        return handle(e)
    
def example2(nums=[0,1,2,3,4]):
    result = [catch(lambda: 1/num) for num in nums]
    print(result)
