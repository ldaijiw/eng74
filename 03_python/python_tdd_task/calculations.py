# py file to be tested

class Calculations:
    # returns True if num1 divided by num2 has no remainder
    def remainder_zero(self, num1, num2):
        if num1 % num2 == 0:
            return True
        return False
    
    # returns True if all numbers passed are positive
    def positive_values(self, *args):
        for num in args:
            if num <= 0:
                return False
        return True