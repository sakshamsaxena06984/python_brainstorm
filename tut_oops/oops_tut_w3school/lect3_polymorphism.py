"""
The word "polymorphism" means "many forms", and in programming it refers to
 methods/functions/operators with the same name that can be executed on many objects or classes.

Polymorphism mainly two types : 1. Method Overloading. 2. Method Overriding.
"""


class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def move(self):
        print("Car_move")


"""
Inheritance Class Polymorphism

Yes. If we use the example above and make a parent class called Vehicle, 
and make Car, Boat, Plane child classes of Vehicle, the child classes inherits 
the Vehicle methods, but can override them
"""


class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def move(self):
        print("Move!")


class Car(Vehicle):
    pass


class Boat(Vehicle):
    def move(self):
        print("Sail!")


class Plane(Vehicle):
    def move(self):
        print("fly")


c1 = Car("Ford", "Mustang")
b1 = Boat("Ibiza", "Touring 20")
p1 = Plane("Boeing", "747")

print("******** polymorphism *********")

for x in (c1, b1, p1):
    print(f"checking the inherited method of {x} is {x.move()}")
    print("-----------")

"""
  x.move()
Child classes inherits the properties and methods from the parent class.

In the example above you can see that the Car class is empty, but it inherits brand, model, and move() from Vehicle.

The Boat and Plane classes also inherit brand, model, and move() from Vehicle, but they both override the move() method.

Because of polymorphism we can execute the same method for all classes.
"""

print("*******  scope in python ***********")
"""
If you operate with the same variable name 
inside and outside of a function, Python will treat 
them as two separate variables, one available in the global scope (outside the function) and 
one available in the local scope (inside the function):
"""

x = "global_variable"


def help():
    x = "local_variable"
    print(f"inside the function : {x}")


help()
print(f"outside the function : {x}")

"""
Global Keyword
If you need to create a global variable, but are stuck in the local scope, you can use the global keyword.

The global keyword makes the variable global.

"""

def help1():
    global x
    x = "global_variable_v1"
    print(f"inside the function : {x}")

help1()

print(f"after modification global value is : {x}")

"""
Nonlocal Keyword
The nonlocal keyword is used to work with variables inside nested functions.

The nonlocal keyword makes the variable belong to the outer function.
"""

def nonlocalfun():
    y = "Jane"
    def nonlocalfunv1():
        nonlocal y
        y="hello"
    nonlocalfunv1()
    return y

print(f"value of y in nonlocal keyword scope : {nonlocalfun()}")

"""
What is a Module?
Consider a module to be the same as a code library.

A file containing a set of functions you want to include in your application.
"""
print("***** little bit module concept ******")

import platform

x = platform.system()
print(x)

x = dir(platform)
print(x)
