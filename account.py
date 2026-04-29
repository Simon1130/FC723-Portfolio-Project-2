#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 28 20:53:12 2026

@author: simon
"""

class Account:
    def __init__(self, username, password, binary_balance, num_tries):
        self.username = username
        self.password = password
        self.binary_balance = binary_balance
        self.num_tries = num_tries
        self.is_locked = False
        
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
        return ans
    def dec_to_32bit2scompliment(money):
        
        if money < 0 :
            money *= -1
#
            
            first_bin = decimal_to_binary(money)
            while len(first_bin) < 32 :
                first_bin = '0' + str(first_bin)
            
#swap all 0's and 1's
            swapped=""
            for bit in first_bin:
                if bit=='0':
                    swapped+='1'
                elif bit == '1' :
                    swapped += '0'
                    
            plus1 = binary_to_decimal(swapped) +1
            output = decimal_to_binary(plus1)
            
            while len(output) < 32 :
                output = '0' + str(output)
            
        else:            
            first_bin = decimal_to_binary(money)
            while len(first_bin) < 32 :
                output = '0' + str(first_bin)
            
        return output
    
    def _2scompliment_to_decimal(binary):
        if binary[0] == "0":
            return binary_to_decimal(binary)
        else:
            first_minus1 = binary_to_decimal(binary) - 1
            minus1_to_bin = decimal_to_binary(first_minus1)
            
            while len(minus1_to_bin) < 32:
                minus1_to_bin = "0" + minus1_to_bin
            
#swap all 0's and 1's again
            swapped=""
            for bit in minus1_to_bin:
                if bit=='0':
                    swapped+='1'
                elif bit == '1' :
                    swapped += '0'
            
            output = binary_to_decimal(swapped) * -1
            return output
    
    def check_balance(self):
        
    def deposit_money(self, money):
        
    def withdraw_money(self, money):
        
