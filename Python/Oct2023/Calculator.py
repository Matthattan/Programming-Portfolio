# Declare Variables
checkpoint1, checkpoint2, checkpoint3 = True, True, True
operators = ["+","-","*","/","**","^","%","//"]


# Requires first input to be numerical (decimal or integer)
while checkpoint1:
    try:
        number1 = float(input("Enter first Number"))
        checkpoint1 = False
    except ValueError:
        print("Invalid Data Type")

# Requires second input to be numerical (decimal or integer)
while checkpoint2:
    try:
        number2 = float(input("Enter second Number"))
        checkpoint2 = False
    except ValueError:
        print("Invalid Data Type")

# Requires operator as a singular character (string)
while checkpoint3:
    operatorInput = str(input("Enter an operator"))
    if operatorInput not in operators:
        print("Invalid Operator")
    elif operatorInput in operators:
        checkpoint3 = False
        
#If statements to check which operator was inputted
if operatorInput == '+':
    total = number1 + number2
elif operatorInput == '-':
    total = number1 - number2
elif operatorInput == '*':
    total = number1 * number2
elif operatorInput == '/':
    # check if number1 is being divided by 0 or if itself is 0
    if  number1 == 0 or number2 == 0:
        raise ZeroDivisionError("Cannot divide by z1ero")
    else:
        total = number1 / number2
elif operatorInput == "**" or operatorInput == "^":
    # check if number1 is negative
    if number1 < 0:
        #if so, check if number2 is a float (negative cannot be exponented by a negative)
        try: 
            int(number2)
        except ValueError: 
            print("Exponenting a negative number with a floating point is invalid.")
    total = number1 ** number2
elif operatorInput == "%":
    total = number1 % number2
elif operatorInput == "//":
    total = number1 // number2
else:
    print("something broke lol")

#output result
print(f"{total}")