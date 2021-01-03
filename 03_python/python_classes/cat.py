# create a Cat class
# one function that returns "meow"

# create Cat class
class Cat:
    # set class variables
    species = "Genus Felis"
    likes_dogs = False

    def __init__(self, gender, **kwargs):
        
        # set instance attributes
        self.gender = gender

        for key, value in kwargs.items():
            setattr(self, key, value)

    # class method to return meow
    def meow(self):
        return "meow"

    # property method to automatically set instance name
    @property
    def name(self):
        return [k for k,v in globals().items() if v is self][0]




if __name__ == "__main__":
    # making 2 instances and then displaying info
    tom = Cat("M", colour = "brown")

    print(tom.name)
    print(tom.species)
    print(tom.likes_dogs)
    print(tom.colour)
    print(tom.gender)
    print(tom.meow())

    jerry = Cat("F", mood = "unhappy")
    print(jerry.species)
    print(jerry.name)
    print(jerry.gender)
    print(jerry.mood)
    print(jerry.meow())

    # changing an attribute and reprinting
    jerry.mood = "happy"
    print(jerry.mood)