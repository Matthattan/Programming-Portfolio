from item import Item

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


