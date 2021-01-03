# while loops


# loops with numbers
number = 0
while number < 10:
    print(f"It's working => {number}")
    
    if number == 4:
        break

    number += 1


# user input with while loop

user_prompt = True

while user_prompt:
    age = input("Please enter your age?\n")

    # isdigit() checks if string is all digits
    if age.isdigit() and int(age) < 117:
        user_prompt = False
    
    else:
        print("Please provide age in digits\n")

print(f"Your age is {age}")