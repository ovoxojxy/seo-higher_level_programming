#!/usr/bin/python3

import unittest
import Base

class TestBase(unittest.TestCase):
    '''Tests the Base class.'''

    def setUp(self):
        '''Imports module, instantiates class'''
        base.Base._Base__nb_objects = 0
        pass

    def tearDown(self):
        '''Cleans up after each test_method.'''
        pass

    def test_A_nb_objects_private(self):
        '''Tests if nb_objects is private class attribute.'''
        self.assertTrue(hasattr(base.Base, "_Base__nb_objects"))

    def test_B_nb_objects_initialized(self):
        '''Tests if nb_objects initializes to zero.'''
        self.assertEqual(getattr(base.Base, "_Base__nb_objects"), 0)
        
    def test_C_instantiation(self):
        '''Tests Base() instantiation.'''
        b = base.Base()
        self.assertEqual(str(type(b)), "<class 'base.Base'>")
        self.assertEqual(b.__dict__, {"id": 1})
        self.assertEqual(b.id, 1)
    def test_D_constructor(self):
        '''Tests constructor signature.'''
        with self.assertRaises(TypeError) as e:
            base.Base.__init__()
        msg = "Base.__init__() missing 1 required positional argument: 'self'"
        self.assertEqual(str(e.exception), msg)

    def test_D_constructor_args_2(self):
        '''Tests constructor signature with 2 notself args.'''
        with self.assertRaises(TypeError) as e:
            base.Base.__init__(self, 1, 2)
            msg = "Base.__init__() takes from 1 to 2 positional arguments but 3 \ were given"
            self.assertEqual(str(e.exception), msg)
