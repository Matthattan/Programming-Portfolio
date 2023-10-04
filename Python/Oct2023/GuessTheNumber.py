import random

correct = False
guessedNumber = ""
counter = 0

#Generate random integer
number = random.randint(0,100)

#Require guesses whilst in the first While Loop
while not correct:
    #Require integer input whilst in nested While Loop
    while True:
        guessedNumber = input("Guess the Number between 0 and 100 \n")
        if not guessedNumber.isdigit():
            print("Value must be an Integer")
        else:
            guessedNumber = int(guessedNumber)
            break
    
    #Check if Number is within Range
    if guessedNumber < 0 or guessedNumber > 100:
        print("Number out of range. Please enter a number between 0 and 100.")
    else:
        #Check if its higher or lower
        if guessedNumber > number:
            print("Number too high \n")
        elif guessedNumber < number:
            print("Number too low \n")
        else:
            correct = True
        counter += 1

#Display winning stats
print(f"Correct Number. Guesses: {counter}")