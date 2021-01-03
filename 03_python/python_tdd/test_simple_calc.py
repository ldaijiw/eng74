from simple_calc import SimpleCalc
import unittest
#import pytest

# unittest.TestCase works with unittest framework as a parent class
class TestCalc(unittest.TestCase):
    calc = SimpleCalc()
    
    # start each method with keyword test_
    def test_add(self):
        # returns True if 2 + 4 returns 6, otherwise False
        self.assertEqual(self.calc.add(2, 4), 6)

    def test_subtract(self):
        self.assertEqual(self.calc.subtract(4, 2), 2)
    
    def test_multiply(self):
        self.assertEqual(self.calc.multiply(2, 3), 6)
    
    def test_divide(self):
        self.assertEqual(self.calc.divide(10, 2), 5)
        

if __name__ == "__main__":
    new_testcalc = TestCalc()
    