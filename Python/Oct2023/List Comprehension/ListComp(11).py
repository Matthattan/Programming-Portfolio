# Set Comprehension

# use curly brackets to intialise sets
# You can use any iterable when using Set Comp

def example1():
    print({i for i in [1,2,3,4]})
    print({i for i in {1,2,3,4}})
    print({i for i in "Hello World!"})

# Sets are unordered and do not take duplicated values
# Therefore its possible that non-unique items 

# are made in set comprehensions which cause only 1 value to be pass
def example2():
    print({i*3 if i < 3 else i for i in [1, 2, 3, 4, 5]})

