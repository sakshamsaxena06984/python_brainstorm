import numpy as np

a = np.array([[1,2,3,4],[5,6,7,8]])
print(a.ndim)
print(a.shape) # (2, 4) mean 2: dimension & 4 : elements in each dimension


b = np.array([1,2,3,4,5],ndmin=5)
print(b.ndim)
print(b) # [[[[[1 2 3 4 5]]]]]
print(b.shape) # (1, 1, 1, 1, 5) 1: representing [ | similarly 1 also represent [ | 5: elements
