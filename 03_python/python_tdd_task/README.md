# Python TDD Task

**TDD Task**
- Create a new Repo on gihub
- Create a new project in pycharm
- name tdd_test_task
- create a file to write tests
- create a file to write code
- implement sudo coding
- create a README to document the steps to successfully achieve the task

- create a test to check is the number divisible/remainder 0 if True pass the test if False fail
- create a class and method to write code to pass the test

- create a test to check if the given values are positive 
- create a method in the class to pass the test

## Remainder 0
- Method to return True if num1 divided by num2 gives no reminder (i.e. ``num1 % num2 == 0``)
```python
class Calculations:
    # returns True if num1 divided by num2 has no remainder
    def remainder_zero(self, num1, num2):
        if num1 % num2 == 0:
            return True
        return False
```
**2 Test Cases**
- Check that ``num1 = 20, num2 = 5`` returns True (using ``assertTrue``)
```python
class TestRemainder(unittest.TestCase):
    class_inst = Calculations()
    
    # test that remainder_zero returns True for 20 % 5
    def test_remainder_zero(self):
        self.assertTrue(self.class_inst.remainder_zero(20, 5))
```
- Check that ``num1 = 17, num2 = 2`` returns False (using ``assertFalse``)
```python
    # test that remainder_zero returns False for 17 % 2
    def test_remainder_nonzero(self):
        self.assertFalse(self.class_inst.remainder_zero(17, 2))
```

## Positive values
- Method to return True if all numbers passed through are positive
```python
# returns True if all numbers passed are positive
    def positive_values(self, *args):
        for num in args:
            if num <= 0:
                return False
        return True
```

**2 Test Cases**
- Check method returns True when all args are positive
```python
 # test that positive_values returns True for 10, 0.5, 0.1, 0.0001
    def test_positive_values(self):
        self.assertTrue(self.class_inst.positive_values(10, 0.5, 0.1, 0.0001))
```
- Check method returns False when at least one arg is negative
```python
# test that positive_values returns False for 0, -1, -0.01
    def test_negative_values(self):
        self.assertFalse(self.class_inst.positive_values(0))
        self.assertFalse(self.class_inst.positive_values(-0.01))
        self.assertFalse(self.class_inst.positive_values(0.01, 10, -5))
```