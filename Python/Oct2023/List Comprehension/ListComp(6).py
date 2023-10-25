# Dictionary Comprehension
# Dict Comp is more efficient and readable compared to previous methods

#The basics of Dict Comp
def example1(person={"Mike":56, 
                     "John":55, 
                     "James":57}):
    member = {k:v for k,v in person.items()}
    print(member)

# Dictionaries can be created from a range function or list using dict comp
def example2(name=["Mike", "John", "Jordan"]):
    print({i:i for i in range(5)})
    print({i:i for i in name})

# Filtering Condition is available in dict comp
def example3(person={"Mike":56, 
                     "John":55, 
                     "James":57}):
    member = {k:v for k,v in person.items() if v > 55}
    print(member)

# Ternery Expression requires distinguishing between the key and value
def example4(person={"Mike":56, 
                     "John":55, 
                     "James":57,
                     "Jordan":63}):
    member = {k.upper(): 
              v*2 if v > 56 else 
              v for k, v in person.items()}
    print(member)