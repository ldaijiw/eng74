from animal import Animal

class Reptile(Animal):
    def __init__(self):

        # executes init of superclass, to inherit from parent class
        super().__init__()

        self.cold_blooded = True
        self.tetrapod = True
        self.heart_chamber = [3, 4]

    # creating functions for reptile class
    def seek_heat(self):
        return "it's cold out here"

    def hunt(self):
        return "catch a meal"

    def use_venom(self):
        return "if I've got it I'm using it"
    



if __name__ == "__main__":
    joey = Reptile()
    print(joey.spine)
    print(joey.cold_blooded)
    print(joey.hunt())