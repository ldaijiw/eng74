import math

class Calculator:
    def __init__(self):
        
        print("\n\n*****\nCalculator\n*****")
        
        self.running = True

        # continues to ask for new questions until told otherwise
        while self.running:
            self.new_calculation()


    def new_calculation(self):
        # input question, also gets rid of any potential spaces to prevent whitespace errors
        question = input("\nWhat would you like to calculate\n(help for more)\n=>").replace(' ', '')
        
        # checks for mathematical operators or other commands permitted in init description
        if '+' in question:
            # after finding operator assigns 2 numbers accordingly
            self.num1 = question[:question.find('+')]
            self.num2 = question[question.find('+')+1:]

            # checks if either input number given as ans 
            self.check_num_is_ans(self.num1, self.num2)
            
            # performs calculation and assigns to answer attribute
            self.ans = self.add(float(self.num1), float(self.num2))

        elif '-' in question:
            self.num1 = question[:question.find('-')]
            self.num2 = question[question.find('-')+1:]

            self.check_num_is_ans(self.num1, self.num2)

            self.ans = self.subtract(float(self.num1), float(self.num2))
        
        elif '/' in question:
            self.num1 = question[:question.find('/')]
            self.num2 = question[question.find('/')+1:]

            self.check_num_is_ans(self.num1, self.num2)

            self.ans = self.divide(float(self.num1), float(self.num2))

        elif '*' in question:
            self.num1 = question[:question.find('*')]
            self.num2 = question[question.find('*')+1:]
            
            self.check_num_is_ans(self.num1, self.num2)

            self.ans = self.multiply(float(self.num1), float(self.num2))
        
        elif 'divisibleby' in question:
            self.num1 = question[:question.find('divisibleby')]
            self.num2 = question[question.find('divisibleby')+11:]
            
            self.check_num_is_ans(self.num1, self.num2)

            self.ans = self.divisible_by(float(self.num1), float(self.num2))
        
        elif 'cm' in question:
            # if cm detected then converts number from cm to inches
            self.num1 = question[:question.find('cm')]
            self.ans = self.inch_cm_convert(float(self.num1), 'cm')
        
        elif 'inch' in question:
            # if inch detected then converts number from inches to cm
            self.num1 = question[:question.find('inch')]
            self.ans = self.inch_cm_convert(float(self.num1), 'inch')
        
        elif 'area' in question:
            # asks for which shape to calculate area from
            area_question = input("\nWhat shape would you like to calculate the area for?\n(Triangle/Circle)\n")

            # asks for relevant dimensions depending on shape
            if 'triangle' in area_question:
                base = input("\nBase length?\n")
                height = input("\nHeight length?\n")
                print("\nAnswer:\n")
                self.ans = self.triangle_area(float(base), float(height))
            
            elif 'circle' in area_question:
                radius = input("\nRadius length?\n")
                print("\nAnswer:\n")
                self.ans = self.circle_area(float(radius))
        
        # if stop or exit given terminates program
        elif 'stop' in question or 'exit' in question:    
            self.running = False
            print("Goodbye")
            return

        elif 'help' in question:
            self.help()
            return
        
        else:
            print("\nQUESTION NOT RECOGNISED PLEASE TRY AGAIN")
            return
        
        print(self.ans)

    
    def check_num_is_ans(self, num1, num2):
        '''
        If either input number is written as ans, then assign that number to the previous answer that's recorded in memory.
        If no answer is stored in memory then informs user to perform a new calculation.
        '''
        try:
            if num1 == 'ans':
                self.num1 = self.ans
            elif num2 == 'ans':
                self.num2 = self.ans
        except AttributeError:
            print("\nNo answer stored in memory, please enter a new calculation\n")
            self.new_calculation()
            return    
            

    def add(self, num1, num2):
        return num1 + num2
    

    def subtract(self, num1, num2):
        return num1 - num2
    

    def divide(self, num1, num2):
        if num2 == 0:
            return "Undefined"
        return num1 / num2
    

    def multiply(self, num1, num2):
        return num1 * num2
    

    def divisible_by(self, num1, num2):
        '''
        Returns True if num1 is perfectly divisible by num2
        '''
        if num1 % num2 == 0:
            return True
        return False
    
    
    def inch_cm_convert(self, num1, convert_from):
        '''
        Converts between inches and cm
        num1: length to convert
        conver_from: scale to convert from
        '''

        if convert_from == "inch":
            return num1 * 2.54
    
        elif convert_from == "cm":
            return num1 / 2.54

    
    def triangle_area(self, base, height):
        return base * height / 2


    def circle_area(self, radius):
        return math.pi * (radius**2)


    def help(self):
        print("""
    **Options**
+                   Addition
-                   Subtraction
/                   Division
*                   Multiplication
divisible by        Check if a number is divisible by another (returns True/False)
area                Work out the area of a shape
inches/cm           Inch/cm converter
ans                 Answer is also stored in memory and can be used for future calculations
exit/stop           Terminate program

Example input questions:
5 + 7.5
10 * 3
ans + 31
144 divisible by 12
area
12 cm
        """)
    


if __name__ == "__main__":
    new_calculator = Calculator()