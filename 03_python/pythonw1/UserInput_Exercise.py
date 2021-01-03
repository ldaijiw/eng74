# Using input() to get 3 pieces of user data

name = input("What is your name: ")
dob = input("What is your date of birth: ")
age = int(input("How old are you: "))


print(f'Hi {name}, you were born in {dob}, you are {age} years old.')
print('Types of variable:')
print('name: ', type(name))
print('dob: ', type(dob))
print('age: ', type(age))