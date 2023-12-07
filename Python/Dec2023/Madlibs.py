# Approach madlibs using classes

class Madlib:
    def __init__(self, nouns=None, nounAmount=None, verbs=None, verbAmount=None, adjectives=None, adjAmount=None):
        # The story will be stored as a string whilst the other words are compiled in a list for easy storage/access as well as implementation to the story
        # commas have been intentoonally missed out since it throws an error otherwise (???)
        self.nouns: list = nouns,
        self.nounAmount: int = nounAmount
        self.verbs: list = verbs,
        self.verbAmount: int = verbAmount
        self.adjectives: list = adjectives,
        self.adjAmount: int = adjAmount

    def createMadlib(self):
        # Add the words to the story property
        self.verbs = [input("Input Verb: \n") for _ in range(self.verbAmount)]
        self.nouns = [input("Input Noun: \n") for _ in range(self.nounAmount)]
        self.adjectives = [input("Input Adjective: \n") for _ in range(self.adjAmount)]
        
        self.optMadlib()
    
    def optMadlib(self):
        print("I {} to the {} with my {} so I could {} my {} {}".format(self.verbs[0], self.nouns[0], self.nouns[1], self.verbs[1], self.adjectives[0], self.nouns[2]))

Beach = Madlib([], 3, [], 2, [], 1)
Beach.createMadlib()
