
class Account():

    def __init__(self, owner, balance=100):
        self.owner = owner
        self.balance = balance

    def __str__(self):
        return f"Account owner: {self.owner} \n Account balance: ${self.balance}"

    def deposit(self, amt):
        self.balance += amt
        print(self)
        return f'Deposit Accepted in the amt of {amt}'

    def withdraw(self, amt):
        if self.balance >= amt:
            self.balance -= amt
            print(self)
        else:
            print(self)
            print(
                f"Withdrawal amt exceeds balance! You cannot withdraw ${amt}")
            return "Withdrawal amt exceeds balance!"


acct1 = Account('Brad', 250)
acct2 = Account('Eleanor', 400)

print(acct1)
# print(acct2)

print('******************************')

acct1.withdraw(254)
acct1.deposit(55)
