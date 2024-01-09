import csv 

# create a template for objects (a class)

class Item:
    # __init__ initialises the properties in the class
    # see also - magic methods
    # when an object is created using this class, whatever is stated here will be ran

    pay_rate = 0.8 # pay rate after 20% discount
    all = []
    def __init__(self, name: str, price: float, quantity:int = 0 ):

        # assert is used to check if what is happening matches with what is expected (like an if statement)
        # Run validations to the received arguments
        assert price >= 0, f"Price {price} is not greater than 0"
        assert quantity >= 0, f"Quantity {quantity} is not greater than 0"

        self.name = name
        self.price = price
        self.quantity = quantity

        # Actions to execute 
        Item.all.append(self)

        print(f"an Instance called {self.name} has been created")

    # Python calls self which is the object that the method is acting from
    def calculate_total_price(self): 
        return self.price * self.quantity
    
    def apply_discount(self):
        return self.price * self.pay_rate # use self.pay_rate to look at the instance level first and then the class instance if its not available
    
    # we can use .csv file to create dynamic instances
    @classmethod
    def instantiate_from_csv(cls):
        # read content as a list of dictionaries
        with open('Programming-Portfolio\Python\Jan2024\OOP\items.csv', 'r') as f:
            reader = csv.DictReader(f)
            items = list(reader)

        for item in items:
            Item(
                name=item.get('name'),
                price=float(item.get('price')), # type casted to float because its a price
                quantity=int(item.get('quantity')) # type casted to int because it describes the amount
            )

    @staticmethod
    def is_integer(num):
        # count all decimals that are integers
        if isinstance(num, float): # compares the var num to the class float
            return num.is_integer() # if true, check if its an integer
        elif isinstance(num, int):
            return True
        else:
            return False

    def __repr__(self): # __repr__ is used to describe how a instance should be displayed when printed
        return f"{self.__class__.__name__} {self.name}: £{self.price}"
        # without this, it would output the data address of the instance

# creating a sub class (child class) from the Item class
class Phone(Item):
    all = []
    def __init__(self, name: str, price: float, quantity:int = 0, broken_phones: int = 0 ):
        # we can use super to inherit values from the parent class
        super().__init__(
            name, price, quantity
        )
        # assert is used to check if what is happening matches with what is expected (like an if statement)
        # Run validations to the received arguments
        assert price >= 0, f"Price {price} is not greater than 0"
        assert quantity >= 0, f"Quantity {quantity} is not greater than 0"
        assert broken_phones >= 0, f"Broken Phones {broken_phones} is not greater or equal to "

        self.name = name
        self.price = price
        self.quantity = quantity
        self.broken_phones = broken_phones

        # Actions to execute 
        Phone.all.append(self)

        print(f"an Instance called {self.name} has been created")

item1 = Item("HP Laptop", 900, 2) 
item2 = Item("Mitsubishi", 100, 5)
item3 = Item("Mac", 750, 3)
item4 = Item("Hotpoint", 2000, 1)
item5 = Item("Dell", 250, 4)
print(type(item1)) # Returns <class "__main__.Item">

print(item1.pay_rate) # pay rate has not been defined in the __init__ method so the the variable is searched for one level up (class level)

print(Item.__dict__) # prints all attributes on class level
print(item1.__dict__) # prints all attributes on instance level

item1.pay_rate = 0.7  # overwrite the pay rate
print(item1.apply_discount())

Item.instantiate_from_csv()
print(Item.all)

print(Item.is_integer(7.05))

phone1 = Phone("iPhone10", 500, 4)
phone1.broken_phones = 1
phone2 = Phone("SamsungS10", 600, 3)
phone1.broken_phones = 1

print(phone1.calculate_total_price())

print(Phone.all)
