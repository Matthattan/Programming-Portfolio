import csv 

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

        self.__name = name # double underscore makes the attribute private
        self.price = price
        self.quantity = quantity

        # Actions to execute 
        Item.all.append(self)

        print(f"an Instance called {self.name} has been created")

    # get name
    @property
    def name(self):
        return self.__name
    # set name
    @name.setter
    def name(self, value):
        self.__name = value

    # Python calls self which is the object that the method is acting from
    def calculate_total_price(self): 
        return self.price * self.quantity
    
    def apply_discount(self):
        return self.price * self.pay_rate # use self.pay_rate to look at the instance level first and then the class instance if its not available
    
    # we can use .csv file to create dynamic instances
    @classmethod
    def instantiate_from_csv(cls):
        # read content as a list of dictionaries
        with open('Programming-Portfolio\Python\Jan2024\OOP\BasicsOfOOP\items.csv', 'r') as f:
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

    @property
    def read_only_name(self):
        return "AAA"