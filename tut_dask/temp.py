import dask.array as darray
import numpy as np

my_array = darray.arange(16, chunks=5)
print(my_array.compute())
print(my_array.chunks)

np_array =  np.arange(15)
print(np_array)

second_array = darray.from_array(np_array, chunks = 5)
print(second_array.compute())
print(f"sum of second_array by dash : {second_array.sum().compute()}")
