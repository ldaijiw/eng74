# Classes, Objects, and Instances

#good naming convention is required, with a capital letter
class Dog:
    animal_kind = "canin"

    # initialising an instance of the class
    def __init__(self, name , colour):
        self.name = name
        self.colour = colour

# define class method
    def bark(self):
# self refers to current instance
        return "woof"

# Create an instance of the class
fido = Dog()

print(fido.animal_kind)
print(fido.bark())

# Create a second instance of the class with its own properties
lassie = Dog()
lassie.animal_kind = "small canin"
print(lassie.animal_kind)