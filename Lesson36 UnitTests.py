# -*- coding: utf-8 -*-
"""
Created on Thu May 28 17:34:17 2020

@author: Christopher Cheng

"""
"""
Focus on debugging and testing
"""

import unittest

""" Takes in a class to work with"""
class TestMyCode (unittest.TestCase):
    def test_add (self):
        """ Returns true if LS = RS"""
        self.assertEqual(2+2,4)
    def test_sub(self):
        """ Returns false if LS = RS"""
        self.assertNotEqual(2-2, 4)
    
    def test_add_5_5(self):
        self.assertEqual(5+5,10)
    def test_mod_6_2(self):
        self.assertEqual(6%2,0)
    
unittest.main()