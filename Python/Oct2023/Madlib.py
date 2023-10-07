import random

class Adventure():
    def __init__(self):
        self.name = "The Adventure \n"
        self.adjective1 = input("Adjective (of a person): \n")
        self.noun1 = input("Noun (item/entity): \n")
        self.adjective2 = input("Adjective: \n")
        self.adjective3 = input("Adjective: \n")
        self.adjective4 = input("Adjective (of a person): \n")
        self.noun2 = input("Noun (item/entity): \n")
        self.adjective5 = input("Adjective (abstract): \n")
        self.adjective6 = input("Adjective: \n")

    def showLib(self):
        print(f"Once upon a time, in a {self.adjective1} land, there lives a {self.noun1}. \
This {self.noun1} was known for being incredibly {self.adjective2}. \
One day, the {self.noun1} decided to embark on a(n) {self.adjective3} adventure. \
Along the way, they met a(n) {self.adjective4} {self.noun2} and together, they faced many {self.adjective5} challenges. \
In the end, they emerged victorious and returned home as {self.adjective6} heroes.") 

class Silly():
    def __init__(self):
        self.name = "Silly Story \n"
        self.adjective1 = input("Adjective (of a person): \n")
        self.noun1 = input("Noun (item/entity): \n")
        self.verb1 = input("Verb (form of movement): \n")
        self.adjective2 = input("Adjective (descriptive): \n")
        self.adjective3 = input("Adjective (of a person): \n")
        self.noun2 = input("Noun (item/entity): \n")
        self.adjective4 = input("Adjective (descriptive): \n")
        self.noun3 = input("Noun: (item/entity): \n")
        self.adjective5 = input("Adjective (abstract): \n")
        self.adjective6 = input("Adjective (abstract): \n")


    def showLib(self):
        print(f"One night, a(n) {self.adjective1} {self.noun1} decided to {self.verb1} to the {self.adjective2} store.\
On the way, they met a\(n\) {self.adjective3} {self.noun2} who offered them a(n) {self.adjective4} {self.noun3}.\
The {self.noun3} caused quite a(n) {self.adjective5} commotion, but everything turned out {self.adjective6} in the end")

class Vacation():
    def __init__(self):
        self.name = "The Vacation \n"
        self.location1 = input("Location: \n")
        self.adjective1 = input("Adjective: \n")
        self.adjective2 = input("Adjective: \n")
        self.noun1 = input("Noun (item): \n")
        self.adjective3 = input("Adjective: \n")
        self.noun2 = input("Noun (item): \n")
        self.verb1 = input("Verb: \n")
        self.adverb1 = input("Adverb: \n")
        self.noun3 = input("Noun (location/item): \n")

    def showLib(self):
        print(f"I can't wait for our upcoming vacation to {self.location1}.\
I've heard its a(n) {self.adjective1} place with {self.adjective2} {self.noun1} and {self.adjective3} {self.noun2}.\
We plan to {self.verb1} to while enjoying the scenery {self.adverb1}. \
I'm especially excited to try the local {self.noun3}.")

story = random.randint(0,3)

if story == 1:
    print("The Adventure")
    Adventure()
elif story == 2:
    print("Silly Story")
    Silly()
else:
    print("The Vacation")
    Vacation()
