# Enumerate in List Comp

# Enumerate is a built-in function that counts or provides an index for items in an iterable
def example1():
    for i,v in enumerate("Hello World!"):
        print(f'{v} at {i}')
    
    # In a list Comp context
    print([(i,v) for i, v in enumerate("Hello World!")])

# Enumerate can also work for putting key-value pairs in a dictionary or set
def example2():
    print({i:v for i, v in enumerate("Hello World!")})

# Even if both values aren't explicity used, they can be inserted into a tuple
def example3():
    print({i for i in enumerate("Hello World!")})

example3()