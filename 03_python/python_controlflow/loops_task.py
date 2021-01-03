# Loops and lists task

# say hello 10 times
for _ in range(10):
    print("hello")

# create a list of names from user input
list_names = []
num_names = int(input("How many names would you like to input? "))
for i in range(num_names):
    list_names.append(input(f"Name {i+1}? ").title())

print("Names: ", list_names)

# make each name lowercase
list_names_lower = [name.lower() for name in list_names]
print("Lowercase names: ", list_names_lower)

# saving names if they are even
list_names_even = [name for name in list_names if len(name)%2 == 0]
print(list_names_even)