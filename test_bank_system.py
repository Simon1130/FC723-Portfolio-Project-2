#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May  3 10:34:28 2026

@author: simon
"""

from unittest import TestCase
from bank_system import Bank

class TestBank(TestCase):
    def setUp(self):
        self.bank = Bank()
        
    def test_wrong_password_length(self):
        self.bank.create_account("TestUser", "1234", 100)
        user = self.bank.user_dict["TestUser"]
        
        self.assertTrue(len(user.password) >= 8, "Error. Password should be 8 - 16 characters: ")
        