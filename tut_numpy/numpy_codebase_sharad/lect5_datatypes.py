"""
python datatypes:
string | integer| float|boolean|complex

numpy datatypes:
i for integer
b for boolean
u for unsigned integer
f for float
c for complex float
m for timedelta
M for datetime
O for object
S for string
U for unicode string
V for memory
"""
import numpy as np

arr = np.array([1,2,3,4])
print(arr)
print(arr.dtype)  #int64

arr1 = np.array(["ssd","sds"])
print(arr1.dtype) # <U3

# way of define datatype
a = np.array([1,2,4,6], dtype='S')
print(a.dtype)

#way of creating an array with data type of 4 byte int
b = np.array([1,2,3,4], dtype='i4')
print(b.dtype)

c = np.array([1,2,3,4], dtype='i8')
print(c.dtype)


str = np.array(['3','2','3'],dtype='i')
print(str)
print(str.dtype)

# str1 = np.array(['s','2','3'],dtype='i')

#  Converting data type in existing array : astype()
print("===========================")
g=np.array([1.1,2.2,3.4])
print(f"datatype of g : {g.dtype}")
g1=g.astype('i')
print(f"datatype of g1 : {g1.dtype}")
