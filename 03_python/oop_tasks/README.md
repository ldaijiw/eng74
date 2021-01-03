# OOP Tasks

## Task 1: FizzBuzz Game

Simple game to substitute:
- multiples of 3 for fizz
- multiples of 5 for buzz
- multiples of both 3, 5 for fizzbuzz

Create class with option to change fizz, buzz, and max range to count up to.


### Tasks

Core:
* Write a program that prints the numbers from 1 to 100.
* For multiples of three print "Fizz" instead of the number
* For the multiples of five print "Buzz" instead of the number
* For numbers which are multiples of both three and five print "FizzBuzz".

Extra:
* make a new fizzbuzz file and make it functional
* make it so we we can decide which numbers to substitute for fizz and buzz using functions

**SOLUTION NOTES**
- class Fizzbuzz with ``__init__`` method assigning fizz and buzz values (default: 3, 5)
- ``play_game`` method has a default max value of 100, loops through range of 1 to max value and returns different values according to fizzbuzz rules
- added extra feature allowing user to choose different max number for the game to count up to
```python
def play_game(self, max_number = 100):
        print(f"New Game with\nFizz = {self.fizz}\nBuzz = {self.buzz}\n\n")
```

## Task 2: Restaurant Order

Menu and Order class allowing to create multiple menus and allowing customer choice of which menu to order from.

### User Stories

#### 1
**AS a User I want to be able to see the menu in a formated way, so that I can order my meal.**

#### 2
**AS a User I want to be able to order 3 times, and have my responses added to a list so they aren't forgotten**

#### 3
**As a user, I want to have my order read back to me in formated way so I know what I ordered.**

**SOLUTION NOTES**
- Menu class that inherits from dictionary, allowing for easier updating and initalising of menu, with keys (food item) and values (prices)
```python
class Menu(dict):
    def __init__(self, menu_items):
        for food, price in menu_items.items():
            self.update({food: price})
 
```

- ``__str__`` method added to change formatting when called in a print() function
```python
def __str__(self):
        print("\n\n***\nHere's the menu:")

        # prints menu items in nice format with price formatting and capitalisation
        for food, price in self.items():
            print("{}, Price: £{:,.2f}".format(food.title(), price))

        return "Hope you enjoy your visit\n***"
```
- Order class checks for all existing menus, then asks user which menu they'd like to order from 
```python
allowed_menus = [k for k, v in globals().items() if isinstance(v, Menu)]
        
```
```python
self.menu_option = input("\nWhich menu will you be ordering from?\n").lower().replace(' ', '_') + "_menu"
        assert self.menu_option in allowed_menus

        self.menu = [v for k, v in globals().items() if k == self.menu_option][0]
```
- Asks user how many items they'd like to order and which items from the menu that they've selected

## Task 3: Scrabble

Scrabble word score calculator, returning score for word based on scrabble letter values.


### Base Scrabble word calculator instructions 

Given the below scoring create a Scrabble word calculator that will provide the correct scores dependent on the string provided. 

```
text
Letter                             Value
A, E, I, O, U, L, N, R, S, T       1
D, G                               2
B, C, M, P                         3
F, H, V, W, Y                      4
K                                  5
J, X                               8
Q, Z                               10
```

**SOLUTION NOTES**
- Used ``@property`` decorator to calculate the score and return as an attribute
```python
@property
    def score(self):
        score = 0
        for word_letter in self.word:
            # matches each letter in word to one of the keys in letter_scores dict, and adds matching value to score
            score += [letter_value for letters, letter_value in self.letter_scores.items() if word_letter in letters][0]
        return score
```

## Task 4: Calculator

- Build a basic object Orientated Calculator
- **phase 1**: build a simple calculator class containing
- add, subtract, multiply, divide.
- **phase 2**: expand by creating:
- Divisible by method that returns true or false dependent on the outcome
- Work out and return the area of a triangle
- inch to cm converter
- NOTE -> Must be in class and method format

**SOLUTION NOTES**
- Asks user for what calculation they'd like to perform then checks for each operator in the input string, assigning the 2 numbers accordingly
```python
question = input("\nWhat would you like to calculate\n(help for more)\n=>").replace(' ', '')
    
    # checks for mathematical operators or other commands permitted in init description
    if '+' in question:
        # after finding operator assigns 2 numbers accordingly
        self.num1 = question[:question.find('+')]
        self.num2 = question[question.find('+')+1:]

    # checks if either input number given as ans 
    self.check_num_is_ans(self.num1, self.num2)
    
    # performs calculation and assigns to answer attribute
    self.ans = self.add(float(self.num1), float(self.num2))

```
- added ``ans`` allowing previous answer to be stored and used for future calculations
```python
 def check_num_is_ans(self, num1, num2):
        '''
        If either input number is written as ans, then assign that number to the previous answer that's recorded in memory.
        If no answer is stored in memory then informs user to perform a new calculation.
        '''
        try:
            if num1 == 'ans':
                self.num1 = self.ans
            elif num2 == 'ans':
                self.num2 = self.ans
        except AttributeError:
            print("\nNo answer stored in memory, please enter a new calculation\n")
            self.new_calculation()
            return    
```


## Task 5: DNA String Parsing

The Problem:  
A string is simply an ordered collection of symbols selected from some alphabet and formed into a word; the length of a string is the number of symbols that it contains.

An example of a length 21 DNA string (whose alphabet contains the symbols 'A', 'C', 'G', and 'T') is "ATGCTTCAGAAAGGTCTTACG."

**Given**: A DNA string s of length at most 1000 nt.

**Return**: Four integers (separated by spaces) counting the respective number of times that the symbols 'A', 'C', 'G', and 'T' occur in s.

Sample Dataset:

_AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC_
Sample Output:

20 12 17 21

NOTE -> Must be in class and method format

**SOLUTION NOTES**
- Added ``@classmethod`` decorator to allow to create an instance of class from input string
```python
@classmethod
def from_DNA_string(cls, dna_string):
    return cls(dna_string = dna_string.upper())
```

## Task 6: Bank Account

Create an **AccountHolderDetails** class with attributes name, address, age, 

**Inherit** Account holder class into MyAccount

- Create a class called MyAccount which represents a bank account, having as attributes: accountNumber (numeric type), balance.
- Create a constructor () with parameters: accountNumber,  balance.
- Create a Deposit() method which manages the deposit actions.
- Create a Withdrawal() method  which manages withdrawals actions.
- Create an bankFees() method to apply the bank fees with a percentage of 5% of the balance account.
- Create a display() method to display account details.
- Create manageAccount class and import everything from BankAccount class
call all methods in manageAccount class that have are available from parent class
- Create a display() method to display account details.
