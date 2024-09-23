class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance
    
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited: {amount}, New Balance: {self.balance}")
        else:
            print("Invalid deposit amount")
    
    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds!")
        else:
            self.balance -= amount
            print(f"Withdrew: {amount}, New Balance: {self.balance}")


account = BankAccount("John", 1000)
account.deposit(500)
account.withdraw(200)
account.withdraw(1500)  