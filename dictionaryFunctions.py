
# initializing dictionary
dict1 = {'Name': 'Ali', 'Age': 23, 'Class': 'BSCS'}
dict2 = dict(Name='Ali', Age=23, Class='BSCS')
dict3 = dict(zip(['Name', 'Age', 'Class'], ['Ali', 23, 'BSCS']))
dict4 = dict([('Name', 'Ali'), ('Age', 23), ('Class', 'BSCS')])
# dict1, dict2, dict3 and dict4 are types of initialing dictionary, they all results same

# accessing values
print(dict1['Name'])            # Ali
print(dict1['Age'])             # 20
print(dict1['Class'])           # BSCS

# updating dictionary
dict1['Age'] = 22               # update existing entry
dict1['University'] = 'UoK'     # Add new entry

print(dict1['Age'])             # 22
print(dict1['University'])      # UoK

# delete element
del dict1['University']         # remove entry with key 'University'
dict1.clear()                   # remove all the entries and return empty dict
del dict1                       # delete the whole dict

# keys and values functions
dict5 = {'a': 1, 'b': 2, 'c': 3, 'd': 4}

print(dict5.keys())             # 'a' 'b' 'c' 'd'
print(dict5.values())           # 1, 2, 3, 4

# shallow copy
dict6 = dict5.copy()
print(dict6)                    # {'a': 1, 'b': 2, 'c': 3, 'd': 4}

# length of dictionary
print(len(dict5))               # 4

# dictionary concatenation
dict7 = {'e': 5}
dict6.update(dict7)
print(dict6)                    # {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}

# removes a random item
print(dict6.popitem())

# get function
dict5.get('e', 5)               # 5   ;  default value used if key is missing
