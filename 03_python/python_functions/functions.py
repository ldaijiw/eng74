# Create a greeting function

def greeting():
    print("Welcome on board")

# function will only execute if it is called

greeting()
# calling the function will execute the code inside the fn

# function with arguments

# add 2 numbers together
def add(num1, num2):
    return num1 + num2

# subtract 2 numbers
def subtract(num1, num2):
    return num1 - num2

# multiply 2 numbers
def multiply(num1, num2):
    return num1 * num2

# divide 2 numbers
def divide(num1, num2):
    return num1 / num2

# modulo 2 numbers
def modulo(num1, num2):
    return num1 % num2

# raise one number to power of num2
def exponent(num1, num2):
    return num1 ** num2


if __name__ == "__main__":
    print(add(1,2))
    print(subtract(1,2))
    print(divide(5, 0))