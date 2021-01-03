import datetime
from datetime import date
from evaluate_bday import has_bday_passed

# gathering user data
name = input("What is your name?\n").title()
age = int(input("How old are you?\n"))

# asks if user would like to reveal birthday
reveal_bday = True if input("Would you like to tell us your birthday?\n(y/n)\n") == 'y' else False

if reveal_bday:
    # asks for birthday
    birthday = {}
    birthday["year"] = date.today().year
    birthday["month"] = int(input("What month were you born? (MM)\n"))
    birthday["day"] = int(input("What day were you born? (DD)\n"))

    not_had_bday = not has_bday_passed(*birthday.values())

elif not reveal_bday:

    #simply asking if bday has passed
    not_had_bday = True if input("Have you had your birthday yet?\n(y/n)\n") == 'n' else False


# calculate birthyear and birthdate considering whether they've had their birthday or not
birthyear = date.today().year - age - not_had_bday

# message to user
if reveal_bday:
    birthdate = datetime.datetime(birthyear, birthday["month"], birthday["day"])
    timediff_h = (datetime.datetime.now() - birthdate).total_seconds() // 3600
    
    print(f"Hi {name}, you are {age} years old, you were born in {birthyear}. You've been alive for around {timediff_h} hours")

elif not reveal_bday:
    print(f"Hi {name}, you are {age} years old, you were born in {birthyear}. You've been alive for a minimum of {age*365*24} hours")


    
