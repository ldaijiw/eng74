'''
Simple game to substitute:
multiples of 3 for fizz
multiples of 5 for buzz
multiples of both 3, 5 for fizzbuzz
'''

class Fizzbuzz:
    # init with default values for fizz (3), buzz (5) 
    def __init__(self, fizz = 3, buzz = 5):
        self.fizz = fizz
        self.buzz = buzz


    # play game with default max number set to 100
    def play_game(self, max_number = 100):
        print(f"New Game with\nFizz = {self.fizz}\nBuzz = {self.buzz}\n\n")

        # loops through numbers 1 to maximum number and checks each number according to fizzbuzz rules
        for num in range(1, max_number + 1):
            
            if (num%self.fizz == 0) and (num%self.buzz == 0):
                print("FizzBuzz")
            
            elif num%self.fizz == 0:
                print("Fizz")
            
            elif num%self.buzz == 0:
                print("Buzz")
            
            else:
                print(num)

if __name__ == "__main__":
    newgame = Fizzbuzz(fizz = 7, buzz = 9)
    newgame.play_game()