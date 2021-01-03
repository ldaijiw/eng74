from snake import Snake

class Python(Snake):
    def __init__(self):
        super().__init__()

        self.large = True
        self.two_lungs = True
        self.venom = False

    def digest_large_prey(self):
        return "finally some good food"

    def climb(self):
        return "up we go"


if __name__ == "__main__":
    peter = Python()
    print(peter.breathe())
    print(peter.digest_large_prey())
    print(peter.cold_blooded)
    print(peter.hunt())
    