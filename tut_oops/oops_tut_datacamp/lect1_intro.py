"""
OOP: Introduction
Object-oriented programming has some advantages over other design patterns. Development is faster and cheaper,
with better software maintainability. This, in turn, leads to higher-quality software, which is also extensible
with new methods and attributes. The learning curve is, however, steeper. The concept may be too complex for beginners.
 Computationally, OOP software is slower, and uses more memory since more lines of code have to be written.

Object-oriented programming is based on the imperative programming paradigm,
which uses statements to change a program's state. It focuses on describing how a program should operate.
Examples of imperative programming languages are C, C++, Java, Go, Ruby and Python.
This stands in contrast to declarative programming, which focuses on what the computer program should accomplish,
without specifying how. Examples are database query languages like SQL and XQuery, where one only tells the computer
what data to query from where, but now how to do it.

OOP uses the concept of objects and classes. A class can be thought of as a 'blueprint' for objects.
These can have their own attributes (characteristics they possess), and methods (actions they perform).

------------------------

Object Oriented Programming in Python
Is Python Object Oriented?
Python is a great programming language that supports OOP. You will use it to define a class with attributes and methods,
 which you will then call. Python offers a number of benefits compared to other programming languages like Java,
 C++ or R. It's a dynamic language with high-level data types. This means that development happens much faster
 than with Java or C++. It does not require the programmer to declare types of variables and arguments.
 This also makes Python easier to understand and learn for beginners, its code being more readable and intuitive.

------------------------

Class
To define a class in Python, you can use the class keyword, followed by the class name and a colon. Inside the class,
an __init__ method has to be defined with def. This is the initializer that you can later use to instantiate objects.
It's similar to a constructor in Java. __init__ must always be present! It takes one argument: self, which refers to
the object itself. Inside the method, the pass keyword is used as of now, because Python expects you to type something
there.
"""


class Dog:
    def __init__(self):
        pass


"""
Note: self in Python is equivalent to 'this' in C++ or Java.
Instantiating objects
To instantiate an object, type the class name, followed by two brackets. 
You can assign this to a variable to keep track of the object.
"""

ozzy = Dog()
print(type(ozzy))  # <class '__main__.Dog'>
