class Bank_Account:

    all_accounts = []

    def __init__(self,int_rate,balance=0):
        self.int_rate = int_rate
        self.balance = balance
        Bank_Account.all_accounts.append(self)

    def deposit(self,amount):
        self.balance += amount
        return self

    def withdraw(self,amount):
        self.balance -= amount
        return self
    
    def display_balance(self):
        print(f"Your balance is: {self.balance}")

    def yield_interest(self):
        if self.balance > 0:
            self.balance = round((self.int_rate * self.balance),2)
            return self
        else:
            print("Account has a negative balance")

    @classmethod
    def print_account_info(cls):
        sum = 0
        for account in cls.all_accounts:
            sum += account.balance
        return sum


account1 = Bank_Account(.07, 1000)
account2 = Bank_Account(.07, 5000)

account1.deposit(50).deposit(25).deposit(200).withdraw(150).yield_interest().display_balance()
account2.deposit(100).deposit(1300).withdraw(50).withdraw(90).withdraw(100).withdraw(25).yield_interest().display_balance()

total_balances = Bank_Account.print_account_info()
print(total_balances)