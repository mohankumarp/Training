#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      MohanKumarP
#
# Created:     20/12/2015
# Copyright:   (c) MohanKumarP 2015
# Licence:     <your licence>
#-------------------------------------------------------------------------------

class BankAccount:
    def __init__(self): #constructor
        self.balance = 0
    def withdraw(self, amount):
        self.balance -= amount
        return self.balance
    def deposit(self, amount):
        self.balance += amount
        return self.balance

class MinimumBalanceAccount(BankAccount):
    def __init__(self, minimum_balance):
        BankAccount.__init__(self) #calling base class constructor
        self.minimum_balance = minimum_balance

    def withdraw(self, amount):
        if self.balance - amount < self.minimum_balance:
            print 'Sorry, minimum balance must be maintained.'
        else:
            BankAccount.withdraw(self, amount)

def main():
    pass

if __name__ == '__main__':
    a = BankAccount()
    b = BankAccount()
    a.deposit(100)
    print a.balance
    b.deposit(50)
    print b.balance
    b.withdraw(10)
    print b.balance
    a.withdraw(10)
    print a.balance
