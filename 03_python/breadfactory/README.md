# TDD Bread Factory

## The Task
### Summary

TDD bread factory is the latest bread brand in Py Land. It always produces the best bread because it has the best testing strategy!

What they do is before they make any new bread, they make a test to make sure the end output is correct. Then they adjust the recipe until it's just right!

You are going to do the same with bread! This is called Test Driven Development.

### Tasks

This exercise is going to bring together lots of concepts.

#### Learning Outcomes
Learning outcomes include:
- git
- github
- functions
- TDD
- Separation of concerns - this is important do not ignore!
- DRY code
- DOD


### Installing and running
To run the naan factory do the following:

```python
import naan factory
run factory()
```


#### TDD - test driven development

1. write the test
2. run it, and read the error
3. code and make it pass the test

this helps with:
- Stop over engineering
- Maintainable code
- Reduce technical debt
- Goes well with agile and working code
- errors can be your guide in complex systems

How it works is that we write unit tests.

###### Unit Tests

Test single pieces of code. Like a function.

**base of a test**
Usually has 3 phases.
- setup phase (know variables)
- calling of the function / piece of code with know variables
- asserting for expect output

#### User stories for Naan Factory

```
#1
As a user, I can use the make dough with 'water' and 'flour' to make 'dough'.

#2
As a user, I can use the bake dough with dough to get naan.

#3
As a user, I can user the run factory with water and flour and get naan.

```

### Acceptance Criteria

* you have written tests
* test pass
* you have written more test to make sure everything works as indented
* all user stories are satisfied
* code does not break
* code has exit condition
* DOD if followed

## SOLUTION NOTES

2 Files created:
- ``test_breadfactory.py``: File for test cases for main code
- ``breadfactory.py``: File for main functionality of bread factory


### test_breadfactory.py

As per user stories outlined above, test py file should contain 3 test methods for each user story.

After importing necessary packages and initialising test class
```python
from breadfactory import BreadFactory
import unittest

class TestBreadFactory(unittest.TestCase):
    factory = BreadFactory()

```

**TESTING make_dough METHOD**
- If _water_ and _flour_ are passed as arguments (regardless of capital letters), expect ``make_dough`` method to return _dough_
```python
# test that make_dough returns 'dough' if 'water' and 'flour' passed as arguments
    def test_make_dough(self):
        self.assertEqual(self.factory.make_dough('water', 'flour'), 'dough')
        self.assertEqual(self.factory.make_dough('WATER', 'Flour'), 'dough')
        self.assertNotEqual(self.factory.make_dough('sugar', 'flour'), 'dough')
```

**TESTING bake_dough METHOD**
- If _dough_ passed as an argument (regardless of capital letters), expect ``bake_dough`` method to return _bread_
```python
  # test that bake_dough returns 'bread' if 'dough' passed as argument
    def test_bake_dough(self):
        self.assertEqual(self.factory.bake_dough('dough'), 'bread')
        self.assertEqual(self.factory.bake_dough('DOUGH'), 'bread')
```

**TESTING run_factory METHOD**
- If _water_ and _flour_ are passed as arguments (regardless of capital letters), expect ``run_factory`` method to return ``True`` (i.e. bread has been successfully made)
```python
    # test that run_factory returns True (i.e. bread successfully made) if 'water' and 'flour' passed as arguments
    def test_run_factory(self):
        self.assertTrue(self.factory.run_factory('water', 'flour'))
        self.assertTrue(self.factory.run_factory('WATER', 'Flour'))
```

**RUN TESTS USING THE TERMINAL COMMAND**
```
pytest -v
```
### breadfactory.py

- Create class ``BreadFactory`` with the following methods: ``make_dough``, ``bake_dough``, ``run_factory``
    - To satisfy user stories and test cases, will need to accept any ingredient and convert to lower case:
```python
ingredients = [item.lower() for item in ingredients]
```
- Then check that the correct ingredients have been supplied in order to perform the relevant action

```python
class BreadFactory:
    
    def make_dough(self, *ingredients):
        print("\nMAKING DOUGH")
        # change all items to lowercase
        ingredients = [item.lower() for item in ingredients]
        # will only return dough if water and flour contained ingredient
        if 'water' in ingredients and 'flour' in ingredients:
            return 'dough'
        return 'Water and flour needed to make dough'
    

    def bake_dough(self, *ingredients):
        print("\nBAKING")
        # change all items to lowercase
        ingredients = [item.lower() for item in ingredients]
        # will only return bread if dough contained in ingredients
        if 'dough' in ingredients:
            return 'bread'
        return 'dough not supplied'


    def run_factory(self, *ingredients):
        # change all items to lowercase
        ingredients = [item.lower() for item in ingredients]
        
        # will attempt to make and bake dough
        product = self.make_dough(*ingredients)
        baked_product = self.bake_dough(product)

        # returns True only if final product is bread
        if baked_product == 'bread':
            print("\nSUCCESSFULLY PRODUCED BREAD")
            return True
        
        return 'Water and flour needed to make bread'
```

**TASK IS SUCCESSFUL IF ALL TESTS ARE PASSED**
```
======================================================================================================= test session starts ========================================================================================================
platform win32 -- Python 3.8.1, pytest-6.1.2, py-1.9.0, pluggy-0.13.1 -- c:\users\daiji\appdata\local\programs\python\python38\python.exe
cachedir: .pytest_cache
rootdir: C:\Users\daiji\Desktop\sparta\breadfactory
collected 3 items

test_breadfactory.py::TestBreadFactory::test_bake_dough PASSED                                                                                                                                                                [ 33%]
test_breadfactory.py::TestBreadFactory::test_make_dough PASSED                                                                                                                                                                [ 66%]
test_breadfactory.py::TestBreadFactory::test_run_factory PASSED                                                                                                                                                               [100%]

======================================================================================================== 3 passed in 0.31s =========================================================================================================
(venv) 
```