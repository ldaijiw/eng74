# py file containing tests

from calculations import Calculations
import unittest

class TestRemainder(unittest.TestCase):
    class_inst = Calculations()
    
    # test that remainder_zero returns True for 20 % 5
    def test_remainder_zero(self):
        self.assertTrue(self.class_inst.remainder_zero(20, 5))
    
    # test that remainder_zero returns False for 17 % 2
    def test_remainder_nonzero(self):
        self.assertFalse(self.class_inst.remainder_zero(17, 2))

    # test that positive_values returns True for 10, 0.5, 0.1, 0.0001
    def test_positive_values(self):
        self.assertTrue(self.class_inst.positive_values(10, 0.5, 0.1, 0.0001))
    
    # test that positive_values returns False for 0, -1, -0.01
    def test_negative_values(self):
        self.assertFalse(self.class_inst.positive_values(0))
        self.assertFalse(self.class_inst.positive_values(-0.01))
        self.assertFalse(self.class_inst.positive_values(0.01, 10, -5))