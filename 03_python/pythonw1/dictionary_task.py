# creating a dictionary to store user details

# Task
# create a New dictionary to store user details
# all the details that you utilised in the last task name, DOB, Address, course, grades, 
# methods of dictionary to remove, add, replace, display the type of items
# create a list of hobbies of at least 3 items 
# display data in revers order of hobby list


user_details = {}

user_details["first name"] = input("What is your first name? ").title()

user_details["last name"] = input("What is your last name? ").title()

user_details["age"] = int(input("How old are you? "))

user_details["dob"] = input("When were you born? ")

user_details["address"] = input("What is your address? ").title()

user_details["course"] = input("What course did you complete? ").title()

user_details["grade"] = input("What grade did you achieve? ")

user_details["hobbies"] = []

while True:
    hobby = input("Do you have any hobbies? Type stop to to complete. ").lower()
    if hobby == "stop":
        break
    else:
        user_details["hobbies"].append(hobby)

user_details["hobbies"].reverse()
print(user_details)

# remove item
user_details.pop("last name")
print(user_details)

# replace age
user_details["age"] = 50
print(user_details)

# showing data types
user_details_datatypes = {key: type(value) for key, value in user_details.items()}

print(user_details_datatypes)