# age restrictions for film

# create a program using control flow with if, elif and else
# using operators == >=
# check age distinctions before selling the ticket
# 18,15 U, 12, PG, 
# else block should ensure to display message if other conditions do not match


age = int(input("How old are you? "))

if age >= 18:
    print("You can watch any film")
elif age >= 15:
    print("Can only watch up to 15")
elif age >= 12:
    print("Can only watch up to 12")
elif age > 0:
    print("Can only watch U and PG")
else:
    print("Invalid age")