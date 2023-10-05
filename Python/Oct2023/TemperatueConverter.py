Input1Status = True
Input2Status = True
Input3Status = True

print("""Welcome to Temperature Converter
What would you like to convert from (1-3)""")

#Sanitise Input 1 - What Unit to convert from
while Input1Status:
    TempUnit1 = input("1. Celsius \n2. Fahrenheit \n3. Kelvin \n")

    try:
        TempUnit1 = int(TempUnit1)
    except:
        print("Error: Value not an Integer")

    if TempUnit1 not in (1,2,3):
        print("Input must be an integer between 1 and 3 (Inclusive)")
    else:
        Input1Status = False

print("What would you like to convert this temperature to (1-3)")

#Sanitise Input 2 - What Unit to convert to
while Input2Status:
    TempUnit2 = input("1. Celsius \n2. Fahrenheit \n3. Kelvin \n")

    try:
        TempUnit2 = int(TempUnit2)
    except:
        print("Error: Value not an Integer")

    if TempUnit2 not in (1,2,3):
        print("Input must be an integer between 1 and 3 (Inclusive)")
    else:
        Input2Status = False

TemperatueInput = float(input("Input the value of the temperatue \n"))

if TempUnit1 == TempUnit2:
    Conversion = TemperatueInput
elif TempUnit1 == 1 and TempUnit2 == 2:
    Conversion = TemperatueInput*(9/5) + 32
elif TempUnit1 == 1 and TempUnit2 == 3:
    Conversion = TemperatueInput + 273.15
elif TempUnit1 == 2 and TempUnit2 == 1: 
    Conversion = (TemperatueInput - 32) * 5/9
elif TempUnit1 == 2 and TempUnit2 == 3:
    Conversion = ((TemperatueInput - 32) * 5/9) + 273.15
elif TempUnit1 == 3 and TempUnit2 == 1:
    Conversion = TemperatueInput - 273.15
elif TempUnit1 == 3 and TempUnit2 == 2:
    Conversion = ((TemperatueInput - 273.15) * 9/5) + 32
else:
    print("Invalid Input")

print(f'{Conversion}')