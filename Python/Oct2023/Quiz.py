quiz = {
    "question1": {
        "question" : "What is a group of Ravens called?",
        "answer" : "a murder"
    },
    "question2": {
        "question" : "What is the 2nd closest Planet to the Sun?",
        "answer" : "venus"
    },
    "question3": {
        "question" : "What is the thousandth value of pi?",
        "answer" : "1"
    },
    "question4": {
        "question" : "What is the capital of Australia",
        "answer" : "canberra"
    },
    "question5": {
        "question" : "What do you put in a toaster?",
        "answer" : "bread"
    },
    "question6": {
        "question" : "True or False - Japan is an archipelago",
        "answer" : "true"
    },
    "question7": {
        "question" : "Where is water on the pH scale?",
        "answer" : "7"
    },
    "question8": {
        "question" : "Who created the modern day periodic table as we know it today?",
        "answer" : "dmitri mendeleev"
    },    
    "question9": {
        "question" : "What musical note is 7 semitones above the note E?",
        "answer" : "b"
    },
    "question10": {
        "question" : "Yes or No - Is this sentence grammatically correct: Do you want to go to the movies with Dave and I?",
        "answer" : "no"
    },  
}

score = 0

for key, value in quiz.items():
    print(value['question'])
    answer = input("\n")

    if answer.lower() == value['answer'].lower():
        score += 1

print(f"Score: {score*10} % ")
print(score)
