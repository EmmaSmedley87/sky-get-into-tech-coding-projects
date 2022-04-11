from debitaccount import DebitAccount

account1 = DebitAccount()
account1.cardType()
account1.openAccount()
account1.deposit()
account1.deposit()
account1.withdraw()

try:
    account1.withdraw()
except FundExceptions as err:
    print("Error occured", err._balance)