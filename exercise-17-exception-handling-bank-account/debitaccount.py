from account import Account

class DebitAccount(Account):

    def __init__(self):
        super().__init__()

    def cardType(self, accountType = "Debit"):
        super().cardType(accountType)
