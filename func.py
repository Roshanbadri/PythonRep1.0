# -*- coding: utf-8 -*-
"""
Created on Mon Aug 13 09:50:01 2018

@author: RO389222
"""

balance=0
amount=0

def withdraw(amount):
    #global amount;
    #balance=0
    if amount > balance:
        raise RuntimeError('Amount greater than available balance.')
    balance -= amount
    return balance

def deposit(amount):
    #global amount
    #balance=0
    balance += amount
    return balance
bal=deposit(1000)
print bal
newbal=withdraw(100)
print newbal
