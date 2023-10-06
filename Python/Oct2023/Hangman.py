#We need the random library for this one
import random

def hangman():
    #Defining Variables
    letters = []
    guessedLetters = []
    Guesses = 7
    #The list of words the program chooses from
    words = [
        "cat",
        "dog",
        "bird",
        "house",
        "apple",
        "banana",
        "chair",
        "table",
        "book",
        "pen",
        "shoe",
        "ball",
        "hat",
        "car",
        "tree",
        "sun",
        "moon",
        "star",
        "fish",
        "cake",
        "flower"]

    #Generate a random word from list
    chosenWord = words[random.randint(0, len(words) - 1)]

    #Sort each letter into an array
    for letter in chosenWord:
        letters.append(letter)

    #Main Game Logic
    while True:
        #Check if the user has already guessed
        if len(guessedLetters) > 0:
            print("Guesses Letters: ")
            print(guessedLetters)
            print(f"Chances: {Guesses} ")
        else:
            print(f"No Attempts yet - {Guesses} chances ")
        
        print(f"Number of Letters: {len(chosenWord)}")
        guessedInput = str(input("Guess the Word \n"))
        
        #If the user has inputted the word
        if guessedInput == chosenWord:
            print(f"You Win! The Word was {chosenWord} and you had {Guesses} Guesses remaining")
            break
        
        for i in guessedInput:
            #If letters match the guessed word then add it to an array
            if i in letters:
                #Make space for the letters if needed
                indexOfLetter = letters.index(i)
                while len(guessedLetters) <= indexOfLetter:
                    guessedLetters.append(" ")
                guessedLetters[indexOfLetter] = i
                letters[indexOfLetter] = " "
                print(indexOfLetter)
            #Else its wrong
            else:
                print("Incorrect!")
                Guesses -= 1

        #End game if guesses is 0
        if Guesses == 0:
            print(f"You lost! The word was {chosenWord}")
            break
        else:
            continue

    restart = str(input("Replay? Y/N \n"))

    if restart == "Y":
        return True
    else:
        return False

#Recursion  
if hangman():
    hangman()
else:
    print("Game Ended, Reload Program to Play again!")


    


        



