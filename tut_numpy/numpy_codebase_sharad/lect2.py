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

y = np.array((2,3,4)) # we are using tuple
print(y)
print(type(y))

# Dimensions in numpy arrays

o_d = np.array(23)
print(o_d)
print((type(o_d)))

#2d arrays

d_2=np.array([[1,2,3],[4,5,6]])
print(d_2)
print(type(d_2))

#3d arrays

d_3=np.array([[[1,2,3],[4,5,6]],[[7,8,9],[17,18,19]]])
print(d_3)
print(type(d_3))

print("***  way of checking dimension in of numpy array [ndim] *******")
print(o_d.ndim)
print(d_2.ndim)
print(d_3.ndim)

d_5=np.array([1,2,3,4],ndmin=5)
print(d_5)
print(d_5.ndim)
