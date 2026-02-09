class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"{amount} deposited. New balance: {self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient balance!")
        else:
            self.balance -= amount
            print(f"{amount} withdrawn. New balance: {self.balance}")

# Example
account = BankAccount("Arjun")
account.deposit(1000)
account.withdraw(500)
account.withdraw(600)