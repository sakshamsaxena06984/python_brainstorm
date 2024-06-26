import pandas as pd

a = [1,2,3]
arr = pd.Series(a)
arr_label = pd.Series(a,index=["a","b","c"])
print(arr)
print(arr_label)
dict = {"rohan":1,"sohan":2,"naman":3}
arr_dict = pd.Series(dict)
print(arr_dict)
arr_dict_index = pd.Series(dict, index=["rohan","naman"])
print(arr_dict_index)

data_set = {
    "rohan":[1,23,3],
    "sohan":[9,3,4]
}

df = pd.DataFrame(data_set)
print(df)
print(df.loc[0])
print(df.loc[[1,2]])
