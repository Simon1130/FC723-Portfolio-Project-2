#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May  3 23:04:15 2026

@author: simon
"""

from bank_system import Bank

def main():
    bank = Bank()
    
    while True:
        print("Welcome to the Bank.")
        print("1. Create Account \n 2.Login Account \n 3.Exit")
        select = input("Please enter your choice in number: ")
        
        if select == "1":
            username = input("Please enter your Username: ")
            password = input("Please enter your password(8 and 16 characters):  ")
            if len(password) > 16 or len(password) < 8:
                password = input("Error. Password should be 8 - 16 characters: ")
            
            balance = float(input("Please enter your initial balance: "))
            
            bank.create_account(username, password, balance)
            print("Account created.")
        
        if select == "2":
            username = input("Please enter Username: ")
            user = bank.get_user(username)
            
            if user is None:
                print("User not found")
                continue
            
            logged_in = False
            while user.num_tries < 3 and user.is_locked == False:
                password = input(f"Please enter the password {3 - user.num_tries} tries left: ")
                check = bank.login(user, password)
                
                if check == True:
                    logged_in = True
                    break
                
                elif check == False:
                    print("Account is locked")
                    break
                
                else:
                    print("Password not correct")
                    
            if logged_in == True:
                while True:
                    print(f"Username: {user.username} Balance: {user.check_balance()}")
                    print("1.Deposit \n 2.Withdraw \n 3.Transfer \n 4.Exit")
                    choice = input("Please enter your choice in number: ")
                    
                    if choice == "1":
                        amount = float(input("Please enter the amount you want to deposit: "))
                        user.deposit_money(amount)
                    
                    if choice == "2":
                        amount = float(input("Please enter the amount you want to withdraw: "))
                        user.withdraw_money(amount)
                    
                    if choice == "3":
                        to_who = input("Please enter the Username you transferring to: ")
                        amount = float(input("The amount: "))
                        
                        output = bank.transfer_money(user, to_who, amount)
                        print(output)
                    
                    elif choice == "4":
                        break
                        
                        
        elif select == "3":
            break

main()
