import numpy as np

# reshape from 1d to 2d
a = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
a1 = a.reshape(4,3)
print(a)
print(a1)
print(f"dimension of a is : {a.ndim}")
print(f"dimension of a1 is : {a1.ndim}")

a3=a.reshape(2,3,2)
"""
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12] = [1, 2, 3, 4, 5, 6] + [7, 8, 9, 10, 11, 12]
[1, 2, 3, 4, 5, 6] = [1,2], [3,4], [5,6] 
[7, 8, 9, 10, 11, 12] = [7,8], [9,10], [11,12]

"""
print("----------------------------------")
print(a)
print("----------------------------------")
print(a.reshape(2,6)) # it is copy
print("----------------------------------")
print(a.reshape(2,6).base)  # it is view  [view, always direct to the actual instance]
print("----------------------------------")

print("******* unknown dimension ********")

print(a.reshape(2,2,-1))
print("----------------------------------")
print(a.reshape(2,1,-1))

print("-----------------conversion into 1 dimensional array -----------------")

a_2d= np.array([[1,2,3],[5,6,7]])
print(a_2d)
print(a_2d.reshape(-1))
