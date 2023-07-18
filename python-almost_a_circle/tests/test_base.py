#!/usr/bin/python3

import unittest
import base.py

class testBase(unittest.TestCase):

    def test__init__(self):
        b = base.Base()
        self.asserIsNotNone(b)
