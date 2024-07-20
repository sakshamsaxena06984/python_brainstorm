"""
Python Classes/Objects
Python is an object oriented programming language.

Almost everything in Python is an object, with its properties and methods.

A Class is like an object constructor, or a "blueprint" for creating objects.

"""


class MyClass():
    x = 5


"""
Create Object
Now we can use the class named MyClass to create objects:
"""
p1 = MyClass()
print(p1.x)
"""
The __init__() Function
The examples above are classes and objects in their simplest form, and are not really useful in real life applications.

To understand the meaning of classes we have to understand the built-in __init__() function.

All classes have a function called __init__(), which is always executed when the class is being initiated.

Use the __init__() function to assign values to object properties, or other operations that are necessary to do when the object is being created:
Note: The __init__() function is called automatically every time the class is being used to create a new object.
"""

"""
The __str__() Function
The __str__() function controls what should be returned when the class object is represented as a string.

If the __str__() function is not set, the string representation of the object is returned:
"""


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


p1 = Person("John", 36)

print(p1)


# The string representation of an object WITH the __str__() function:

class Persion1:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} and his/her age is {self.age}"

    # adding method
    def myfun(self):
        print("Hello, my name is : " + self.name)


p1 = Persion1("John", 36)

print(p1)
p1.myfun()

"""
The self Parameter
The self parameter is a reference to the current instance of the class, 
and is used to access variables that belongs to the class.
"""

# Modify Object Properties
p1.age = 34

print(f"after modification : {p1}")

# You can delete properties on objects by using the del keyword:
del p1.age

print(f"after deletion : {p1}")

# You can delete objects by using the del keyword:
del p1

"""
The pass Statement
class definitions cannot be empty, but if you for some reason have a class definition with no content, put in the pass statement to avoid getting an error.


"""


class Personempty:
    pass
