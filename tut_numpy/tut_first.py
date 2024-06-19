import numpy as np

arr = np.array([1,2,3,4,5])
print(arr)
print(np.__version__)
print(type(arr))
# 0 DArray
arr_0 = np.array(2)
print(arr_0)
# 1 DArray
arr_1 = np.array([1,2,3,4])
print(arr_1)
# 2 DArray
arr_2 = np.array([[1,2,3],[4,5,6]])
print(arr_2)
# 3 DArray
arr_3 = np.array([[[1,2,3],[4,5,6],[5,6,8],[11,22,44]]])
print(arr_3)
print(f"3_DArray : {arr_3.ndim}")
arr_5 = np.array([1,2,3,5], ndmin=8)
print(arr_5)
print(f" dimensions in arr_5 : {arr_5.ndim}")
print(f" data type array 1_arr : {arr_2.dtype}")

arr_float = np.array([1.1,2.2,3.3])
print(arr_float.dtype)
print(arr_float)
new_arr = arr_float.astype('i')
print(new_arr.dtype)
print(new_arr)
print(arr_2.shape)
print(arr_3.shape)
arr_3_reshape = arr_3.reshape(2,2,-1)
print(arr_3_reshape)
print("=== iterating over the arr_3 ===")
for ele in arr_3:
    print(ele)
print("+++ iterating over the nditer() method +++")
for ele in np.nditer(arr_3):
    print(ele)

print("+++ way of using buffered +++")
print(arr_float)
for ele in np.nditer(arr_float, flags=['buffered'], op_dtypes=['S']):
    print(ele)

print("=== iterating via ndenumerate ===")
for idx,x in np.ndenumerate(arr_3):
    print(idx, x)

print("=== join ===")
a = np.array([[1,2],[3,4]])
b = np.array([[5,6],[7,8]])
arr_join_1 = np.concatenate((a,b), axis=1)
arr_join_0 = np.concatenate((a,b), axis=0)
print(arr_join_1)
print(arr_join_0)

