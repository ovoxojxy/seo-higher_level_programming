#!/usr/bin/python3

import unittest
import Base

class testBase(unittest.TestCase):

    def test__init__(self):
        b = base.Base()
        self.asserIsNotNone(b)

    def test_Base(self):
        id = Base.Base()
        self.assertTrue(id

    def setup(self):
        Base._Base__nb_objects = 0
        pass

    def tearDown(self):
        pass
    
    def test_nb__objects_initialized(self):
        self.assertTrue(hasattr(Base.Base, "_Base__nb_objects"))

    def test_nb_tests(self):
        self.assertEqual(type(getattr(Base, "_Base__nb_objects")), int)

    def test_instantiation(self):
        b = Base.Base()
        self.assertEqual(str(type(b)), "<class 'models.base.Base'>")

if __name__ == "__main__":
    unittest.main()

