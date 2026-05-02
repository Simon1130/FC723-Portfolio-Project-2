#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 29 20:00:40 2026

@author: simon
"""

from unittest import TestCase
from account import Account

class TestAccount(TestCase):
    def setUp(self):
        self.username = "test"
        self.password = "pa33w0rd"
        self.initial_balance = 100
        self.acc = Account(self.username, self.password, self.initial_balance)
    
    def test_initial_balance(self):
        self.assertEqual(self.acc.check_balance(),100)
        
    def test_deposit(self):
        self.acc.deposit_money(10)
        self.assertEqual(self.acc.check_balance(),110)
        
    def test_withdraw_negative(self):
        self.acc.withdraw_money(150)
        self.assertEqual(self.acc.check_balance(),-50)
        
    def test_over_withdraw_limit(self):
        self.acc.withdraw_money(1600)
        over_limit = self.acc.withdraw_money(1)
        self.assertFalse(over_limit)
        self.assertEqual(self.acc.check_balance(),-1500)
        
