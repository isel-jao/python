print("Working with dictionaries")

# Creating a dictionary
my_dict = {'name': 'John', 'age': 30, 'city': 'New York'}
print(my_dict, type(my_dict))  # Output: {'name': 'John', 'age': 30, 'city': 'New York'} <class 'dict'>

# Accessing keys and values
print(my_dict.keys())  # Output: dict_keys(['name', 'age', 'city'])
print(my_dict.values())  # Output: dict_values(['John', 30, 'New York'])


# Iterating over a dictionary
for key, value in my_dict.items():
    print(key, value)

# Checking if a key is present
print('age' in my_dict)  # Output: True

# Adding a new key-value pair
my_dict['occupation'] = 'Engineer'
print(my_dict)  # Output: {'name': 'John', 'age': 30, 'city': 'New York', 'occupation': 'Engineer'}

# Modifying a value
my_dict['age'] = 35
print(my_dict)  # Output: {'name': 'John', 'age': 35, 'city': 'New York', 'occupation': 'Engineer'}

# Removing a key-value pair
del my_dict['occupation']
print(my_dict)  # Output: {'name': 'John', 'age': 35, 'city': 'New York'}

# Safely accessing a value using get()
print(my_dict.get('age'))  # Output: 35

# Clearing the dictionary
my_dict.clear()
print(my_dict)  # Output: {}

# Deleting the dictionary
del my_dict
# print(my_dict)  # This will raise a NameError as the dictionary is deleted

# Creating two dictionaries for set-like operations
dict1 = {'a': 1, 'b': 2, 'c': 3}
dict2 = {'b': 2, 'c': 4, 'd': 5}

# Union of dictionaries (combining unique keys)
union_dict = {**dict1, **dict2}
print(union_dict)  # Output: {'a': 1, 'b': 2, 'c': 4, 'd': 5}

# Intersection of dictionaries (keys common in both)
intersection_dict = {key: dict1[key] for key in dict1.keys() & dict2.keys()}
print(intersection_dict)  # Output: {'b': 2, 'c': 3}

# Difference of dictionaries (keys in dict1 but not in dict2)
difference_dict = {key: dict1[key] for key in dict1.keys() - dict2.keys()}
print(difference_dict)  # Output: {'a': 1}

# Symmetric difference of dictionaries (keys present in only one of the dictionaries)
symmetric_difference_dict = {**{key: dict1[key] for key in dict1.keys() - dict2.keys()}, **{key: dict2[key] for key in dict2.keys() - dict1.keys()}}
print(symmetric_difference_dict)  # Output: {'a': 1, 'c': 4, 'd': 5}
