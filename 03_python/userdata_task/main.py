# userdata_task

'''
using input() to take trainee data from users
using casting and string methods to format them correctly
'''

first_name = input("What is your first name? ").lower().capitalize()

middle_name = input("What is your middle name? ").lower().capitalize()

last_name = input("What is your last name? ").lower().capitalize()

age = int(input("How old are you? "))

address = input("What is the first line of your address? ").lower().title()

postcode = input("Please enter your postcode: ").upper()

ni_number = input("Please enter your NI number: ").upper()

course_applied = input("What course did you apply for? ").lower().title()

most_recent_edu = input("What is your most recent education? ").lower().title()

print(f"Hello {first_name} {middle_name} {last_name}. Your details have been saved.")

while True:
    what_to_print = input("\n\nWhich data would you like to see?\nType stop to stop program.\n").lower()

    if what_to_print == "stop":
        break
    elif what_to_print == "first name":
        print(first_name)
    elif what_to_print == "last name":
        print(last_name)
    elif what_to_print == "age":
        print(age)
    elif what_to_print == "address":
        print(address)
    elif what_to_print == "postcode":
        print(postcode)
    elif what_to_print == "ni number":
        print(ni_number)
    elif what_to_print == "course applied":
        print(course_applied)
    elif what_to_print == "recent education":
        print(most_recent_edu)
    else:
        print("Invalid request, try again or type stop to stop program.")