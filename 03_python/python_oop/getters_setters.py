# getters and setters
# use cases: can use to decide which data is available for use to the user
# hide data: separation of concern

# to get/set information

class Student:
    def __init__(self, name, company):
        self.__name = name
        self.company = company

    @property # A decorator in python is any callable python object that is used to modify a function or class
    def student_name(self):
        
        # double underscore used to hide data
        return self.__name

    @student_name.setter # sets the value
    def student_name(self, value):
        
        self.__name = value


if __name__ == "__main__":
    new_student = Student("Joey", "Sparta")
    print(new_student.__name)
    print(new_student.student_name)