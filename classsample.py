# -*- coding: utf-8 -*-
"""
Created on Thu Aug 16 11:42:02 2018

@author: RO389222
"""

class customer(object):
    def __init__(self,balance,name):
        self.balance=balance
        self.name=name
    def meth(func):
        val = raw_input("Are you sure you want to proceed? Y/N: ")
        if val=='Y':
            return func 
        else:
            exit
        return func   
    #@meth
    def deposit(self,amount):
        self.balance += amount
        return self.balance
    @meth
    def withdraw(self,amount):
        #amount=0
        if amount > self.balance:
            raise RuntimeError('Amount greater than available balance.')
        self.balance -= amount
        return self.balance
if __name__ == '__main__':
    
    cust1=customer(1000,"Roshan")
    #print cust1.balance,cust1.name
    dep=cust1.deposit(200)
    print dep
    balance=cust1.withdraw(100)
    print balance