# Why is there no list comprehension for Tuples?
# the normal brackets are used for generators

# With this in mind, you can use the tuple function to turn a generator expression or a list into a tuple

def example1():
    result1 = tuple((i for i in range(4)))
    result2 = tuple([i for i in range(4)])

    print(result1)
    print(result2)

# You can use an asterisk and a comma to also create a tuple

def example2():
    result1 = *(i for i in range(4)),

    print(result1)
    print(type(result1))

example2()