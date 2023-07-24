#!/usr/bin/python3

import unittest
import base

class testBase(unittest.TestCase):

    def test__init__(self):
        b = Base.Base()
        self.assertIsNotNone(b)

    def test_Base(self):
        id = Base.Base()
        self.assertTrue(id)
        
