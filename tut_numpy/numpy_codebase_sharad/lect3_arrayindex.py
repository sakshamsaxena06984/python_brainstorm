import numpy as np

arr = np.array([1, 2, 3, 4, 5])
print(arr)
print("****  way of getting indexing ******")
print(arr[0])
print(arr[1])
print("way of using operator !")
print(f"sum of index 2 and 3 is : {arr[2] + arr[3]}")

# applying indexing on 2d

arr2 = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9,10]])
print(arr2)
print("using indexing for 2d arrays")
print(f"getting the second elements : {arr2[0, 1]}")

arr3 = np.array([[[1,2,3],[4,5,6]],[[44,55,66],[77,88,99]]])
print(arr3)
print(arr3.ndim)
print(f"getting the 6 value : {arr3[0,1,2]}")


