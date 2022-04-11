from fundexceptions import FundExceptions
# general functionality for accounts
class Account:
    # constructer
    def __init__(self):
        self._balance = 0

# methods
    def openAccount(self):
        print("Your balance is", self._balance)

    def cardType(self, cardType):
        print("This is your", cardType, "account")

    def deposit(self):
        amount = float(input("Enter the amount you are depositing. "))
        print("The amount you deposited is", amount)
        self._balance += amount
        print("Your new balance is", self._balance)

    def withdraw(self):
        withdrawalAmount = float(input("Enter the amount you are withdrawing. "))
        if self._balance >= withdrawalAmount:
            self._balance -= withdrawalAmount
            print("You have withdrawn", withdrawalAmount)
            print("Your balance is now", self._balance)
        elif self._balance < withdrawalAmount:
            raise FundExceptions()
        else:
            print("Insufficient balance")