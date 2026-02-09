class BankAccount:
    def __init__(self, balance):
        self.balance = balance

class SavingsAccount(BankAccount):
    pass

class CurrentAccount(BankAccount):
    pass

s = SavingsAccount(5000)
c = CurrentAccount(10000)

print(s.balance)
print(c.balance)