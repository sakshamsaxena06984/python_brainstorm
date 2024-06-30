"""
Python Classes/Objects
Python is an object oriented programming language.

Almost everything in Python is an object, with its properties and methods.

A Class is like an object constructor, or a "blueprint" for creating objects.

"""
class MyClass():
    x=5

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
