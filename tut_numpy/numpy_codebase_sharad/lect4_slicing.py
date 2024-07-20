"""
slicing in numpy array:
[start:end] or [start:end:step]
"""
import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 8, 9])
print(arr)
print(f"len of array is : {len(arr)}")
print(arr[1:5])
print(arr[0:len(arr)])
print(arr[0:])  # if end value is not present then iteration will reach to the end of an array
print(arr[:5])  # if start value is not present then start will be 0

"""
[1, 2, 3, 4, 5, 6, 8, 9]
-9,-7,-6,-5,-4,-3,-2 ,-1
"""
print("****** Negative Indexing ********")
print(f"Minus indexing : {arr[-3:-1]}")

print("steps in slicing")
print(arr[0::3])
print(arr[::2])

arr2 = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])

print(f"printing 7,8,9 {arr2[1, 1:4]}")
print(arr2.ndim)
print(f"printing 2 and 7 : {arr2[0:2, 1]}")
""" 
                                             index  0,1,2,3,4            0,1,2,3,4
above case is really interesting, 0:2 mean pick 0 ->[1,2,3,4,5] and 1 ->[6,7,8,9,10] 
and ,1 mean, index 1 element value.
"""

print(f"printing [2,3,4],[7,8,9] : {arr2[0:2, 1:4]}")

arr3 = np.array([[[ 1,  2,  3],
                      [ 4,  5,  6],
                      [ 7,  8,  9]],

                     [[10, 11, 12],
                      [13, 14, 15],
                      [16, 17, 18]],

                     [[19, 20, 21],
                      [22, 23, 24],
                      [25, 26, 27]]])
print(arr3)
print(type(arr3))
print(arr3.ndim)

print("----------using slicing in 3D array-------------")
print(arr3[0:3,0:2])
print("----------------------")
print(arr3[:, 1, :])
print("----------------------")
print(arr3[1, :, 2])


print("---------------")
print(arr3[:, :2, :2])
