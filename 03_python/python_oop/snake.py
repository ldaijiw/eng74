from reptile import Reptile

class Snake(Reptile):
    def __init__(self):

        super().__init__()
        self.forked_tongue = True
        self.venom = True
        self.limbs = False

    def use_tongue_to_smell(self):
        return "taste to smell, smell to taste"


if __name__ == "__main__":
    steve = Snake()
    print(steve.breathe())
    print(steve.cold_blooded)
    print(steve.use_tongue_to_smell())