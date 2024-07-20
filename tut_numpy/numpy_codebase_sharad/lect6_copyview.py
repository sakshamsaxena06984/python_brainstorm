import numpy as np

a = np.array([1,2,3,4,5])
a_copy = a.copy()
print(a)
print(a_copy)
print(" after update ")
a_copy[2]=22
print(a)
print(a_copy)
# working with view in numpy

b = np.array([1,2,3,4,5])
b_view = b.view()
print(b)
print(b_view)
print("after update ")
b[2]=234
print(b)
print(b_view)
