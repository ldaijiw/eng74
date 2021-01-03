# Declare a list with numbers 1 to 5 and add 6 at the end
new_list = [1, 2, 3, 4, 5]
new_list.append(6)

# Create a tuple with numbers 1 to 5 and print up to 3
new_tuple = (1, 2, 3, 4, 5)

for num in new_tuple:
    if num > 3:
        break
    print(num)


# Declare a dictionary of a shopping list with 3 items, find what type of data it is
shopping_dict = {"apple": 0.5, "banana": 0.75, "bread": 1}
print(type(shopping_dict))

# find price for one item
print(shopping_dict["bread"])

# replace price for one of the items
shopping_dict["bread"] = 2
print(shopping_dict["bread"])


# Declare function that takes two arguments to add 2 numbers together
def add(num1, num2):
    return num1 + num2

print(add(2,4))


# Create a class called person with name and age
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


new_person = Person("Leo", 21)
print(new_person.name)
print(new_person.age)


# Create a class called student that inherits from person with student_id and course
class Student(Person):
    def __init__(self, name, age, student_id, course):
        super().__init__(name, age)

        self.student_id = student_id
        self.course = course

new_student = Student("Leo", 21, 123, "DevOps")
print(new_student.name)


# Create dictionary with 4 items with prices
shopping_dict2 = {"chicken": 3, "pasta": 1, "rice": 2, "eggs": 1}

# Find total cost
print(sum(shopping_dict2.values()))


# Create function find total cost of dictionary values

def added_dict(dict_arg):
    return sum(dict_arg.values())

print(added_dict(shopping_dict2))

# Super() refers to the parent class, allowing to specifically call methods from the parent class that may have been overwritten

# Add an item in location 3, can not be done as dictionaries are indexed by keys (unordered)
shopping_dict2["juice"] = 2
print(shopping_dict2)




# create a list with same items as before
shopping_list = ["chicken", "pasta", "rice", "eggs"]
print(shopping_list)

# iterate through list, if rice is found within list, break
for item in shopping_list:
    if item == "rice":
        break
    print(item)