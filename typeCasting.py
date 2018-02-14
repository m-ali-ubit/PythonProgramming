
from functools import reduce    # reduce use for dictionary
# converting any data type to another is called type casting.

# string to int

print(int('1'))     # string number
print(ord('a'))     # string character ; convert character to its ASCII code

# int to string
print(str(123))
print(type(str(123)))       # using type function we can find the data type.

# string to float
print(float('2.5'))

# float to string
print(str(4.65))
print(type(str(4.65)))       # using type function we can find the data type.

# float to int
print(int(4.8))

# int to float
print(float(6))

# list to tuple
print(tuple([1, 2, 4, 'x', 8.9]))

# list to dictionary
# as we know dictionary needs two values one for its key and second for its value
print(dict.fromkeys([1, 2, 4, 'x', 'y', 8.9], ))    # leaving second argument means none
print(dict.fromkeys([1, 2, 4, 'x', 'y', 8.9], 5))   # or you can pass a integer or character or a list
print(dict.fromkeys([1, 2, 4, 'x', 'y', 8.9], 'a'))
print(dict.fromkeys(['a', 'b', 'c'], [1, 2, 3]))

# we can convert two lists to dictionary as one for keys and second for values using zip function
# lists should be of same size. if they are not, zip will truncate the longer one
print(dict(zip([1, 2, 3, 4], ['a', 'b', 'c', 'd'])))

# tuple to list
print(list((9, 8, 7, 6)))

# tuple to dictionary
# same as list to dict ; using dict.fromkeys and zip function

# dictionary to list
d = {1: 'a', 2: 'b'}
print(list(d))           # print list of only keys
print(list(d.keys()))    # print list of keys
print(list(d.values()))  # print list of values
print(dict.items(d))     # list of tuples ; each tuple contain key and its value
print(list(reduce(lambda x, y: x + y, d.items())))  # convert all keys and values into one list

# dictionary to tuple
# same as dict to list

# int to complex
print(complex(10, 4))    # complex takes two arguments one for real part second for imaginary
print(complex(10))       # if do not pass second argument function take 0 as default
