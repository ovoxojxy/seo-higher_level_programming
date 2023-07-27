#!/usr/bin/python3

import unittest
from models.base import Base

class testBase(unittest.TestCase):

    def test__init__(self):
        b = base.Base()
        self.asserIsNotNone(b)

    def test_Base(self):
        id = Base.Base()
        self.assertTrue(id)

    def test_nb_tests(self):
        nb = Base.__nb_objects
        self.assertIsInstance(nb, self.base.id)

    def setup(self):
        Base._Base__nb_objects = 0
        pass

    def tearDown(self):
        pass
    
    def test_nb__objects_initialized(self):
        self.assertTrue(hassattr(Base, "_Base__nb_objects"))

    def test_nb__objects_initialized(self):
        self.assertEqual(getattr(Base, "_Base__nb_objects"), 0)

    def test_instantiation(self):
        b = Base()
        self.assertEqual(str(type(b)), "<class 'models.base.Base'>")
        self.assertEqual(b.__dict__, {"id": 1})
        self.assertEqual(b.id, 1)

if __name__ == "__main__":
    unittest.main()

