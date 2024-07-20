"""

Enums (short for Enumerations) are a way to define a set of named values in Python.
They can be used to represent a collection of related constants and provide readability and maintainability
to your code. Enums are available in Python through the enum module
"""
from enum import Enum


class Color(Enum):
    red = 1
    green = 2
    blue = 3


print(Color.red)
print(f"value of Color[red] class : {Color.red.value}")
print(f"name of Color[red] class : {Color.red.name}")

print("***** way of iteration **********")

for ele in Color:
    print(ele)

print(Color.red == Color.red)       # Output: True
print(Color.red == Color.green)     # Output: False
print(Color.red is Color.red)       # Output: True
print(Color.red is not Color.green)

"""
Unique Enum Members:
To ensure that all enum members have unique values, you can use the @unique decorator:
"""


from enum import  unique

@unique
class Color1(Enum):
    red=1
    green=2

"""
Enum with Custom Methods:
Enums can have custom methods just like regular classes:
"""

class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3

    def is_primary(self):
        return self in (Color.RED, Color.GREEN, Color.BLUE)

print(Color.RED.is_primary())   # Output: True
print(Color.GREEN.is_primary()) # Output: True

"""
Auto-assigning Values with auto():
You can use the auto() function to automatically assign values to enum members:
"""
from enum import auto
class Color(Enum):
    RED = auto()
    GREEN = auto()
    BLUE = auto()

print(list(Color)) # Output: [<Color.RED: 1>, <Color.GREEN: 2>, <Color.BLUE: 3>]

