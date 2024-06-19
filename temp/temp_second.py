import pandas as pd


data = [1, 2, 3, 4, 5]

# Create a DataFrame
# df = pd.DataFrame(data, columns=['Values'])
df = pd.DataFrame(data)

# Print the DataFrame
print(df)

ans = df.describe()
print(ans)
print(f"type of ans is : {type(ans)}")
print(f"")
