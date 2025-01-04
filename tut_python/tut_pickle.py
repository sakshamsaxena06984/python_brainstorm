import pickle

# Example object (a dictionary)
data = {'name': 'Alice', 'age': 25, 'city': 'New York'}

# Pickling (Saving the object to a file)
with open('data.pickle', 'wb') as file:
    pickle.dump(data, file)  # dump serializes the object and writes it to the file

# Unpickling (Loading the object back from the file)
with open('data.pickle', 'rb') as file:
    loaded_data = pickle.load(file)  # load deserializes the object from the file

print(loaded_data)  # Output: {'name': 'Alice', 'age': 25, 'city': 'New York'}
