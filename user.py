from typing import _SpecialForm


class User:
    
    def __init__(self, fname, lname):
        self.fname = fname 
        self.lname = lname
        self.account_balance = 0
    
    def make_deposit(self, money):
        self.account_balance += money
        return self

    def make_withdrawal(self, money):
        self.account_balance -= money
        return self

    def display_user_balance(self):
        print( self.fname, self.account_balance)
        return self
    
    def make_a_transfer(self, reciever, amount):
        reciever = reciever
        self.account_balance -= amount
        reciever.account_balance += amount
        print(self.fname, self.account_balance) 
        print(reciever.fname, reciever.account_balance)   
        return self



alan = User( 'Alan', 'Sobenes')
joe = User('Joe', 'Dirt')
Mike = User('Mike', 'Tyson')





alan.make_deposit(1000).make_deposit(5000).make_deposit(2500).make_withdrawal(1500).display_user_balance() 


joe.make_deposit(300).make_deposit(200).make_withdrawal(10).make_withdrawal(10).display_user_balance()



Mike.make_deposit(50).make_withdrawal(15).make_withdrawal(20).make_withdrawal(20).display_user_balance()

alan.make_a_transfer(joe, 700) 

