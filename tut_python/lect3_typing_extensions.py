"""

ChatGPT
The from typing_extensions import overload statement in Python is used to import the overload decorator
from the typing_extensions module. This decorator is utilized to define function and method overloads in
a way that is compatible with type checkers like mypy.

Use of @overload
When you have a function that can accept different types of arguments
and return different types based on those arguments, you can use the @overload decorator to provide
type hints for each possible signature. This helps type checkers understand
how the function should behave with different types of inputs.


"""
def func(x):
    if isinstance(x, int):
        return x+1
    # elif isinstance()
