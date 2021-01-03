# creating an Animal class as PARENT/BASE/SUPER class

class Animal:
    def __init__(self):
        self.alive = True
        self.spine = True
        self.lungs = True
        self.eyes = True
    
    def breathe(self):
        return "Keep breathing to stay alive"

    def move(self):
        return "left to right and up and down"

    def eat(self):
        return "hungry"
    
    def procreate(self):
        return "find partner"

if __name__ == "__main__":
    # instance of Animal
    cat = Animal()

    print(cat.eat())
