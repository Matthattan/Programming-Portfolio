# create a template for objects (a class)

class Item:
    # __init__ initialises the properties in the class
    # see also - magic methods
    # when an object is created using this class, whatever is stated here will be ran
    def __init__(self, name: str, price: float, quantity:int = 0 ):

        # assert is used to check if what is happening matches with what is expected (like an if statement)
        # Run validations to the received arguments
        assert price >= 0, f"Price {price} is not greater than 0"
        assert quantity >= 0, f"Quantity {quantity} is not greater than 0"

        self.name = name
        self.price = price
        self.quantity = quantity

        print(f"an Instance called {self.name} has been created")

    # Python calls self which is the object that the method is acting from
    def calculate_total_price(self): 
        return self.price * self.quantity

item1 = Item("HP Laptop", 900, -2) 
print(type(item1)) # Returns <class "__main__.Item">

item2 = Item("iPhone", 1500, -5)

# Returns the total cost of all quantity of laptops (price * quantity)
print(item1.calculate_total_price(item1.price, item1.quantity)) 
print(item2.calculate_total_price(item2.price, item2.quantity))