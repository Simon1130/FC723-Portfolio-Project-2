#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 28 20:53:12 2026

@author: simon
"""

class Account:
    def __init__(self, username, password, binary_balance, is_locked, num_tries):
        self.username = username
        self.password = password
        self.binary_balance = binary_balance
        self.is_locked = is_locked
        self.num_tries = num_tries
        
    def decimal_to_binary(n):
    
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
    
    def binary_to_decimal(n):
        ans = 0
        power = 0
        
        for i in reversed(str(n)):
            if i == '1':
                ans += 2**power
                power += 1
            else:
                power += 1
        return ans
    def dec_to_32bit2scompliment(money):
        ans = 0
        
        if money < 0 :
            money *= -1
#n += 1
            
            ans = decimal_to_binary(money)
            while len(ans) < 32 :
                ans = '0' + str(ans)
            
#swap all 0's and 1's
            swapped=""
            for bit in ans:
                if bit=='0':
                    swapped+='1'
                elif bit == '1' :
                    swapped += '0'
                    
            ans = binary_to_decimal(swapped) +1
            output = decimal_to_binary(ans)
            
            while len(ans) < 32 :
                ans = '0' + str(ans)
            if len(ans) > 32:
                ans = ans[-32:]
            
        else:            
            ans = decimal_to_binary(money)
            while len(ans) < 32 :
                output = '0' + str(ans)
            
        return output
    
    def check_balance(self):
        
    def deposit_money(self, money):
        
    def withdraw_money(self, money):
        
