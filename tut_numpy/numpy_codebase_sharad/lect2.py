# ways of creating NumPy ndArrays
"""
Note: The array object in numpy is call ndarray

"""
import numpy as np

x = np.array([1, 2, 3, 4])
print(type(x))  # <class 'numpy.ndarray'>
print(x)

"""
we can also pass a list, tuple or any array like object with array(), and it will be converted to ndarray
"""
y = np.array((1,2,3,4))
print(y)
print(type(y)) # <class 'numpy.ndarray'>
