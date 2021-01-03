# file for test cases for breadfactory.py

from breadfactory import BreadFactory
import unittest

class TestBreadFactory(unittest.TestCase):
    factory = BreadFactory()

    # test that make_dough returns 'dough' if 'water' and 'flour' passed as arguments
    def test_make_dough(self):
        self.assertEqual(self.factory.make_dough('water', 'flour'), 'dough')
        self.assertEqual(self.factory.make_dough('WATER', 'Flour'), 'dough')
        self.assertNotEqual(self.factory.make_dough('sugar', 'flour'), 'dough')


    # test that bake_dough returns 'bread' if 'dough' passed as argument
    def test_bake_dough(self):
        self.assertEqual(self.factory.bake_dough('dough'), 'bread')
        self.assertEqual(self.factory.bake_dough('DOUGH'), 'bread')
    
    
    # test that run_factory returns True (i.e. bread successfully made) if 'water' and 'flour' passed as arguments
    def test_run_factory(self):
        self.assertTrue(self.factory.run_factory('water', 'flour'))
        self.assertTrue(self.factory.run_factory('WATER', 'Flour'))