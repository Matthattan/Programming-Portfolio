# list comp vs Generators
import sys
from timeit import timeit

# Generators are what happen when, instead of square brackets to surround a list comp, normal brackets are used
# referring to Generators gets you the memory location instead of the result
def example1():
    a = [x for x in range(100)]
    b = (x for x in range(100))
    print(a)
    print(b)

    # using a Generator is far more memory efficient compared to a normal list since its an expression and not the actual result
    print(sys.getsizeof(a))
    print(sys.getsizeof(b))

# Generators are also quite time efficient by a huge margin
def example2():
    print(timeit("[x for x in range(100)]"))
    print(timeit("(x for x in range(100))"))
    print(timeit("(x for x in range(1000))"))

# Generators don't use the same functions are lists e.g. append
def example3():
    a = [x for x in range(100)]
    b = (x for x in range(100))

    a.append(100)
    print(a)

    try:
        b.append(100)
        print(b)
    except AttributeError:
        print("Not Possible")

