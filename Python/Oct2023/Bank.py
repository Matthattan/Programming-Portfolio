class User():
    def __init__(self, name, age, ID):
        self.name = name
        self.age = age
        self.ID = ID

    def showDetails(self):
        print(f"""
Personal Details:
{self.name}
{self.ID}
""")
        

class Bank(User):
    def __init__(self, name, age, ID):
        super().__init__(name, age, ID)
        self.balance = 0

    def deposit(self, amount):
        self.balance += amount
        print(f"""
Account Balance: 
{self.balance}
""")
        
    def withdraw(self, amount):
        self.amount = amount
        if self.amount > self.balance:
            print(f"""
Insufficient Funds
Balance Available:
{self.balance}""")
        else:
            self.balance -= self.amount
            print(f"""
Withdrawal Made:
{self.amount}                 
Balance Available:
{self.balance}""")  

    def viewBalane(self):
        self.showDetails()
        print(f"Account Balance: \n {self.balance}")