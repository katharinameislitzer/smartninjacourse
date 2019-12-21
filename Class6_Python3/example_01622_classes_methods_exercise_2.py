# create a class bank account
# it has 2 fields: name and balance
# it has methods to withdraw and deposit and print statement


class BankAccount(object):
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def print_statement(self):
        print(str(self.name) + ",your balance is " + str(self.balance))

    def withdraw_money(self, amount):
        self.balance -= amount

    def deposit_money(self, amount):
        self.balance += amount


account = BankAccount("Kathi", 100)
account.print_statement()
account.withdraw_money(200)
account.print_statement()
account.deposit_money(200)
account.print_statement()