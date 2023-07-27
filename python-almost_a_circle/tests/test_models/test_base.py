#!/usr/bin/python3


import unittest
from models.base import Base

class testBase(unittest.TestCase):

    def setUp(self): 
        Base._Base__nb_objects = 0
        pass

    def teardown(self):
        pass
                                
    
    def test___init__(self):
        b = Base()
        self.assertEqual(str(type(b)), "<class 'models.base.Base'>")
        self.assertEqual(b.__dict__, {"id": 1})
        self.assertEqual(b.id, 1)

    def test_Base(self):
        id = Base.Base() 
        self.assertTrue(id)
    
    def test_nb_tests(self):
        nb = Base._Base__nb_objects
        self.assertIsInstance(nb, self.base.id)

    def test___nb_objects_attr(self):
        self.assertTrue(hasattr(Base, "_Base__nb_objects"))

    def test___nb_objects_initalized(self):
        self.assertEqual(getattr(Base, "_Base__nb_objects"), 0)
    
    def test_D_constructor(self):
        with self.assertRaises(TypeError) as e:
            Base.__init__()
        msg = "__init__() missing 1 required positional argument: 'self'"
        self.assertEqual(str(e.exception), msg)


    def test_D_constructor_args_2(self):
        with self.assertRaises(TypeError) as e:
            Base.__init__(self, 1, 2)
        msg = "__init__() takes from 1 to 2 positional arguments but 3 \
        were given"
        self.assertEqual(str(e.exception), msg)
                
    def test_E_consecutive_ids(self):
        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.id + 1, b2.id)
                    
    def test_F_id_synced(self):
        b = Base()
        self.assertEqual(getattr(Base, "_Base__nb_objects"), b.id)
    
    def test_F_id_synced_more(self):
        b = Base()
        b = Base("Foo")
        b = Base(98)
        b = Base()
        self.assertEqual(getattr(Base, "_Base__nb_objects"), b.id)
                            
    def test_G_custom_id_int(self):
        i = 98
        b = Base(i)
        self.assertEqual(b.id, i)
                                
    def test_G_custom_id_str(self):
        i = "FooBar"
        b = Base(i)
        self.assertEqual(b.id, i)
    
    def test_G_id_keyword(self):
        i = 421
        b = Base(id=i)
        self.assertEqual(b.id, i)
