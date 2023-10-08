def binarySearch(array, target, low=None, high=None):
    if low is None:
        low = 0
    if high is None:
        high = len(array) - 1

    if high < low:
        return "Item not Found"

    midpoint = (low + high) // 2

    if array[midpoint] == target:
        return f"Item found at {midpoint}"
    elif target < array[midpoint]:
        return binarySearch(array, target, low, midpoint-1,)
    else:
        return binarySearch(array, target, midpoint+1, high)
    
array = []
count = 0

while True:
    try:
        #Ask how many values the use wants to input
        amount = int(input("Insert amount of Items \n"))
        break
    except ValueError:
        # Validation
        print("Invalid Input - Enter a Number")

while count < amount:
    #Start appending items to array
    array.append(int(input("Enter an Item. The Full list must be in numerical order \n")))
    count += 1

#ask for target item
target = int(input("What item are you looking for? \n"))
#Run function to return item position
print(binarySearch(array, target))