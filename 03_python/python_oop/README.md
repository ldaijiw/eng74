# Object Oriented Programming

### Superclasses and Subclasses

**Step 1**
- Create an animal class as our parent

**Step 2**
- create reptile class as the child class
- why? so we can inherit from our parent
- abstract

**Step 3**
- create snake class as child of reptile

**Step 4**
- create a Python class

``__name__`` and ``__main__`` are used to check if the code is run from the current file/directly or for a different file/importing it

### Name == Main
```
if __name__ == "__main__":
    pass
```
This is only true if the code running is the current file.

### Getters and Setters

Getters and setters are decorators used for class methods to return a class attribute, whilst hiding sensitive data. For example:
```
class Student:
    def __init__(self, name, company):
        self.__name = name
        self.company = company
```
``self.__name`` is a private attribute and will raise an error if the user tries to call it, claiming it does not exist; compared to ``self.company`` which can be accessed as normal.

```
print(student_obj.__name) # raises an error
```

Using getters and setters allows the user to access attributes whilst still withholding direct access to ``self.__name``

**GETTER**
```
@property
def student_name(self):
    return self.__name
```
The ``@property`` decorator acts as the getter
```
print(student_obj.student_name) # returns name
```

**SETTER**
```
@student_name.setter
def student_name(self, new_name):
    self.__name = new_name
```
The ``student_name.setter`` decorator allows the user to set __name indirectly.
```
student_obj.student_name = "alex"
# sets student_obj.__name to "alex"
```

Other uses can be to change related attributes at the same time, for example the radius and diameter of a circle. 

```
class Circle:
    def __init__(self, radius):
        self.radius = radius

    
    @property
    def diameter(self):
        return self.radius * 2

    @diameter.setter
    def diameter(self, new_diameter):
        self.radius = new_diameter/2
```

Changing radius will automatically alter diameter, and vice versa
