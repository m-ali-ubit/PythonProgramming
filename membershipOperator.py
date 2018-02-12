
# python offers a very helpful operators called membership it checks whether a value is present or not
# in a given sequence, such as strings, lists or tuples and returns TRUE or FALSE

string = 'hello world'
lst = [1, 2, 3, 4, 5]
tupl = (6, 7, 8, 9, 10)

# 'in' operator
print('b' in string)    # False
print('h' in string)    # True
print(6 in lst)         # False
print(2 in lst)         # True
print(6 in tupl)        # True
print(2 in tupl)        # False

# 'not in' operator
print('b' not in string)    # True
print('h' not in string)    # False
print(6 not in lst)         # True
print(2 not in lst)         # False
print(6 not in tupl)        # False
print(2 not in tupl)        # True
