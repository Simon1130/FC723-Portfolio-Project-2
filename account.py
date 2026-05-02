#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 28 20:53:12 2026

@author: simon
"""

class Account:
    def __init__(self, username, password, initial_balance):
        self.username = username
        self.password = password
        self.binary_balance = self.dec_to_32bit2scompliment(initial_balance)
        self.num_tries = 0
        self.is_locked = False
        
    def decimal_to_binary(self, n):
    
        if n == 0:
            return "0"
#make a list to store answer
        ans = []
#loop till n reach 1
        while n >= 1:
#if n is even 
            if n % 2 == 0:
    
                n //= 2 
                ans.append(str(0))
                
            else:
                
                n //=2
                ans.append(str(1))
                
                
        ans.reverse()
        ans = ''.join(ans)
        return ans
    
    def binary_to_decimal(self, n):
        ans = 0
        power = 0
        
        for i in reversed(str(n)):
            if i == '1':
                ans += 2**power

            power += 1
        return ans
    
    def dec_to_32bit2scompliment(self, money):
        
        if money < 0 :
            money *= -1
#
            
            first_bin = self.decimal_to_binary(money)
            while len(first_bin) < 32 :
                first_bin = '0' + str(first_bin)
            
#swap all 0's and 1's
            swapped=""
            for bit in first_bin:
                if bit=='0':
                    swapped+='1'
                elif bit == '1' :
                    swapped += '0'
                    
            plus1 = self.binary_to_decimal(swapped) +1
            output = self.decimal_to_binary(plus1)

            
        else:            
            output = self.decimal_to_binary(money)
            
        while len(output) < 32 :
            output = '0' + str(output)
            
        return output
    
    def _2scompliment_to_decimal(self, binary):
        binary = str(binary)
        if binary[0] == "0":
            return self.binary_to_decimal(binary)
        else:
            first_minus1 = self.binary_to_decimal(binary) - 1
            minus1_to_bin = self.decimal_to_binary(first_minus1)
            
            while len(minus1_to_bin) < 32:
                minus1_to_bin = "0" + minus1_to_bin
            
#swap all 0's and 1's again
            swapped=""
            for bit in minus1_to_bin:
                if bit=='0':
                    swapped+='1'
                elif bit == '1' :
                    swapped += '0'
            
            output = self.binary_to_decimal(swapped) * -1
            return output
    
    def check_balance(self):
        return self._2scompliment_to_decimal(self.binary_balance)
        
    def deposit_money(self, deposit):
        current_balance = self.check_balance()
        new_balance = current_balance + deposit
        self.binary_balance = self.dec_to_32bit2scompliment(new_balance)
        return f"Remaining: {new_balance}"
    
    def withdraw_money(self, withdraw):
        current = self.check_balance()
        if current - withdraw < -1500:
            print("Error. Limit exceeded.")
            return False
        else:
            new_balance = current - withdraw
            self.binary_balance = self.dec_to_32bit2scompliment(new_balance)
            print(f"Remaining: {new_balance}")
            return True
        