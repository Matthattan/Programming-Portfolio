# Approach madlibs using classes

class Madlib:
    def __init__(self, nouns=None, nounAmount=None, verbs=None, verbAmount=None, adjectives=None, adjAmount=None):
        # The story will be stored as a string whilst the other words are compiled in a list for easy storage/access as well as implementation to the story
        self.nouns: list = nouns,
        self.nounAmount: int = nounAmount,
        self.verbs: list = verbs,
        self.verbAmount: int = verbAmount
        self.adjectives: list = adjectives,
        self.adjAmount: int = adjAmount

    def createMadlib(self):
        # Add the words to the story property
        self.verbAmount = self.verbAmount

        self.verbs = [input("Input Verbs") for _ in range(self.verbAmount)]
        
        print(self.optMadlib())
    
    def optMadlib(self):
        return f'I {self.verbs[0]} to the Beach with my {self.verbs[1]}'
        

Beach = Madlib([], 1, [], 2)
Beach.createMadlib()
