from tkinter import messagebox


class BalanceException(Exception):
    pass


class BankAccount:
    def __init__(self, initial_amount: int, acc_name: str):
        self.balance = initial_amount
        self.name = acc_name
        print(f"\nAccount '{self.name}' created.\nBalance = {self.balance:.3f}$")

    def getBalance(self):
        print(f"\nAccount '{self.name}' balance = {self.balance} $")

    def deposit(self, amount):
        self.balance = self.balance + amount
        print(f"\n deposit completed !")
        self.getBalance()

    def viableTransaction(self, amount):
        if self.balance >= amount:
            return
        else:
            raise BalanceException(f"\n Sorry, account '{self.name}' only has a balance of {self.balance:.3f}$")

    def withdraw(self, amount):
        try:
            self.viableTransaction(amount)
            self.balance = self.balance - amount
            print("\n withdraw completed !")
            self.getBalance()
        except BalanceException as error:
            print(f"\n withdraw interrupted {error}")

    def transfer(self, amount, account):
        try:
            print("\n***************\nTransferring.....\n***************")
            self.viableTransaction(amount)
            self.withdraw(amount)
            account.deposit(amount)
            print("\n***************\nTransfer completed !\n***************")
        except BalanceException as error:
            print(f"\n Transfer interrupted.{error}")


class InterestRewardsAccount(BankAccount):
    def deposit(self, amount):
        self.balance = self.balance + (amount * 1.05)
        print("\n Deposit completed !")
        self.getBalance()


class SavingAccount(InterestRewardsAccount):
    def __init__(self, initialamount, accname):
        super().__init__(initialamount, accname)
        self.fee = 5

    def withdraw(self, amount):
        try:
            self.viableTransaction(amount + self.fee)
            self.balance = self.balance - (amount + self.fee)
            self.getBalance()
        except BalanceException as error:
            print(f"\n Withdraw interrupted: {error}")
