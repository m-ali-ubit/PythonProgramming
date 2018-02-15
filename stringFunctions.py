
string1 = 'hello world'
string2 = 'python programming'
print(string1[::2])
# substring
print(string1[0:5])     # hello
print(string2[7:14])    # program

# substring using slicing
print(string1[::2])     # hlowrd    ;   here 2 is the slicer which shows that it prints every second letter

# length of string
print(len(string1))     # 11
print(len(string2))     # 18

# string update
print(string1[:5] + ' python')

# string concatenation
print(string1 + string2)    # hello worldpython programming

# string repetition
print(string1 * 2)      # hello worldhello world

# string formatting
print('my name is %s and age is %d.' % ('Ali', 23))
print('my name is {0} and age is {1}'.format('Ali', '23'))

# string builtin functions
print(string1.capitalize())     # Hello world ; capitalize first word
print(string1.center(20, '-'))  # ----hello world-----
print(string1.count('o'))       # 2 ; no. of 'o' in string1
print(string1.endswith('ld'))   # True ; string1 ends with ld
print(string1.startswith('py'))  # False ; string starts with h
print(string1.find('r'))        # 8 ; r found on index 8 ; if not found returns -1
print(string1.index('d'))       # 10 ; d found on index 10 ; if not found returns exception
print(string1.isalnum())        # string1 is alphanumeric or not
print(string1.isnumeric())      # string1 is numeric or not
print(string1.isalpha())        # string1 contains alphabets only or not
print(string1.isdigit())        # string1 contains digits only or not
print(string1.islower())        # string1 is lower cased or not
print(string1.isupper())        # string1 is upper cased or not
print(string1.istitle())        # string1 is in titled case or not
print('-'.join(string1))        # joins '-' with every character of string1
print(string1.lower())          # converts whole string into lower case
print(string1.upper())          # converts whole string into upper case
print(string1.replace('o', 'i'))  # replace 'o' to 'i' in string1
print(string1.split())          # returns list of words of string
