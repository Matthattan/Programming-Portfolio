# Approach madlibs using classes

class Madlib:
    def __init__(self, story, nouns, nounAmount, verbs, verbAmount, adjectives, adjAmount):
        # The story will be stored as a string whilst the other words are compiled in a list for easy storage/access as well as implementation to the story
        self.story: str = story,
        self.nouns: list = nouns,
        self.nounAmount: int = nounAmount,
        self.verbs: list = verbs,
        self.verbAmount: int = verbAmount
        self.adjectives: list = adjectives,
        self.adjAmount: int = adjAmount

    def createMadlib(self):
        # Add the words to the story property

        self.nouns = [input("Input Nouns") for _ in range(self.nounAmount)]
        

Beach = Madlib(story="I went to the shop", nouns=None, nounAmount=1, verbs=None, verbAmount=None, adjectives=None, adjAmount=None)
Beach.createMadlib()