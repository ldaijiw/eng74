# Examples of built in functions

# import is keyword used to call modules from Python library

import random
import math
import os
import datetime
import sys

# generates a float number from 0 to 1
print(x := random.random())
print(round(x))


# using math.floor to round a number down
num_float = 23.44
print(num_float)
print(math.floor(num_float))

# using math.ceil to round a number up
print(math.ceil(num_float))


'''
Task
get user input of a float number
check if the number is lower than .50 then round the figure to lower end
check if the number is greater than .51 then round the figure to higher end
example - num_float = 23.66 - round it to 24, num_float = 23.50 - round it to lower end
tips - get help online - python library
'''

def round_num():
    num = float(input("What number would you like to round?\n"))

    # simpler method of rounding number
    # return round(num)

    if num % 1 >= 0.5:
        return math.ceil(num)
    return math.floor(num)


# print current working directory
print(os.getcwd())

# number of cpu cores
print(os.cpu_count())

# datetime module gives ability to find current date and time
print(datetime.datetime.today())

# find system path
print(sys.path)

def current_system_path():
    print(f"This is your current system paths")
    return sys.path


print(current_system_path())