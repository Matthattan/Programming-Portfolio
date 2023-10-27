# How to remove empty lists from a list
# List Comp vs Filter func

# using a filtering condition in list comp
def example1(List1=[1,2,3,[],[],"True",4,5, ""]):
    List2 = [x for x in List1 if x]

    # You can specify the condition of the items you're looking for
    List3 = [x for x in List1 if isinstance(x, int)]
    List4 = [x for x in List1 if x != []]

    print(List2)
    print(List3)
    print(List4)

# Using a filter function
def example2(List1=[1,2,3,[],[],"True",4,5, ""]):
    Result1 = list(filter(None, List1))

    # using a Lambda is possible
    Result2 = list(filter(lambda x: x != [], List1))

    print(Result1)
    print(Result2)

example2()