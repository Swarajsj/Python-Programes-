# %%
# Creating a Nested Dictionary
# as shown in the below image

Dict = {1: 'Geeks', 2: 'For', 3: {'A': 'Welcome', 'B': 'To', 'C': 'Geeks'}}
print(Dict)

# %%
# Adding elements one at a time

Dict[0] = 'Geeks'
Dict[2] = 'For'
Dict[3] = 1
print("\nDictionary after adding 3 elements: ")
print(Dict)

# %%
# Adding set of values
# to a single Key

Dict['Value_set'] = 2, 3, 4
print("\nDictionary after adding 3 elements: ")
print(Dict)

# %%
# Updating existing Key's Value

Dict[2] = 'Welcome'
print("\nUpdated key value: ")
print(Dict)

# %%
# Adding Nested Key value to Dictionary

Dict[5] = {'Nested': {'1': 'Life', '2': 'Geeks'}}
print("\nAdding a Nested Key: ")
print(Dict)
