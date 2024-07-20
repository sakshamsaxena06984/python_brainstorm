"""
The getsourcefile function from the inspect module in Python is used to retrieve the filename of the Python
source file where a given object (such as a module, function, class, method, etc.) was defined.
This can be particularly useful for debugging, logging, or when you need to inspect or document the source
code of a specific object.
"""

import inspect

def func():
    pass

source_file=inspect.getsource(func)
print(f"source_file value is {source_file}")

"""
Use Cases
Debugging: Identify where a particular piece of code is located.
Documentation: Automatically generate documentation that includes file locations.
Introspection: Analyze code structure and dependencies.
"""

class ExampleClass:
    def help(self):
        pass
print(f"getting the class info : {ExampleClass}")
print(f"getting the class method info : {ExampleClass.help}")

import math
print(f"getting the math module info : {inspect.getsourcefile(math)}")
