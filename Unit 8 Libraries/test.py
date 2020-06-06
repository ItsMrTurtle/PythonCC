# -*- coding: utf-8 -*-
"""
Created on Thu May 28 18:09:56 2020

@author: Christopher Cheng
"""

import unittest
import funcs

class TestAbs(unittest.TestCase):
    def test_abs_5(self):
        absolute = funcs.abs_val(5)
        self.assertEqual(absolute,5)
    def test_abs_neg5(self):
        absolute = funcs.abs_val(-5)
        self.assertEqual(absolute,5)
    def test_abs_0(self):
        absolute = funcs.abs_val(0)
        self.assertEqual(absolute,0)
        
class TestPrime(unittest.TestCase):
    def test_prime_5(self):
        isprime = funcs.is_prime(5)
        self.assertEqual(isprime,True)
    def test_prime_4(self):
        isprime = funcs.is_prime(4)
        self.assertEqual(isprime,False)
    def test_prime_10000(self):
        isprime = funcs.is_prime(10000)
        self.assertEqual(isprime,False)
        
unittest.main()