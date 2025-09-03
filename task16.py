class Account:
    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("Not enough balance!")

class SavingsAccount(Account):
    def __init__(self, balance=0, interest_rate=0.0):
        super().__init__(balance)
        self.interest_rate = interest_rate

    def calculate_interest(self):
        return self.balance * self.interest_rate

class CheckingAccount(Account):
    pass

s = SavingsAccount(1000, 0.05)
s.deposit(500)
print(s.calculate_interest())

