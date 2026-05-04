#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 28 20:54:30 2026

@author: simon
"""
from account import Account

class Bank:
    def __init__(self):
        self.user_dict = {}
        
    def create_account(self, username, password, balance):
        new_acc = Account(username, password, balance)
        self.user_dict[username] = new_acc #save it to dictionary
    
    def get_user(self, username): #use it in main.py
        return self.user_dict.get(username)
    
    
    

    
    def login(self, user, password):

        if user.is_locked == True:
            print("This account is locked")
            return False
            
        if password == user.password:
            user.num_tries = 0 #initialise number of tries if succes
            return True
        
        else:
            user.num_tries += 1
            
            if user.num_tries >= 3:
                user.is_locked = True
                return False
            return f"Not correct. Remaining tries: {3 - user.num_tries}"
            
            

        
    def transfer_money(self, from_who, to_who, amount):
        
        if to_who not in self.user_dict:
            return "User not found"
        
        if from_who == to_who:
            return "Cannot choose yourself" #avoid bugs if choosing itself
        
        to_who_acc = self.user_dict[to_who] #make it to account class with username
        
        if from_who.withdraw_money(amount) == True:
            to_who_acc.deposit_money(amount)
            return f"£{amount} has transfered to {to_who}."
        
        else:
            return "The amount you transfer exceeded the withdraw limit."
        