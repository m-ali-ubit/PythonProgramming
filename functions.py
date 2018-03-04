
# syntax of function
# def function_name(parameters):
#   """doc string ; its optional"""
#   body
#   return


def add_numbers(x, y):           # takes two parameters x and y and returns their addition
    return x + y

print(add_numbers(5, 7))         # 12


def add_numbers2(x, y, z=None):  # arguments can be pre-defined if pass by object can be replaced
    if z is None:
        return x + y             # if takes two parameters return x+y
    else:
        return x + y + z         # if takes three parameters


print(add_numbers2(1, 2))         # 3
print(add_numbers2(1, 2, 3))      # 6


# types of arguments
# required arguments
def print_number(num):            # here num is necessary to be passed otherwise raise exception
    print(num)
    return

# print_number()                  this will raise TypeError
print_number(10)                  # 10


# keyword arguments
# caller identifies the arguments by the parameter name
def print_numbers(num1, num2):
    print(num1, num2)
    return

print_numbers(num2=5, num1=8)     # values can be define out of order using keywords


# default keywords
# pre-defined value of argument is called default keyword
def detail(name, city, uni='UBIT'):
    print(name, city, uni)
    return

detail('Ali', 'Karachi')                # Ali Karachi UBIT
detail('Ali', 'Karachi', uni='UOK')     # Ali Karachi UOK


# variable-length arguments
# used to handle parameters which are not define in function
# *args is used to handle non-keyword variable length arguments
def var_len(var, *args):
    print(var)
    print(args)
    return

var_len(5)                                  # 5 ()
var_len(5, 1, 2, 3, 'a', 'b', 2.5, 3.6)     # 5 (1, 2, 3 , 'a', 'b', 2.5, 3.6)
var_len(5, [1, 2, 3, 4])                    # 5 ([1, 2, 3, 4])


# an example from book 'learning python'
# find smallest value from passed arguments using *
def minimum(*num):
    if num:
        mini = num[0]
        for value in num[1:]:
            if value < mini:
                mini = value
        print(mini)
    return

minimum(2, 8, 1, -8)        # -8
minimum()                   # nothing prints


# **kwargs is used to handle keyword variable length arguments
def var_len2(var, **kwargs):
    print(var)
    print(kwargs)
    return

var_len2('ok')                              # ok
var_len2('ok', name='Ali', age=23)          # ok {'name': 'Ali', 'age': 23}


# an example from book 'learning python'
# db connection function using **
def connect(**options):
    conn_params = {
        'host': options.get('host', '127.0.0.1'),
        'port': options.get('port', 5432),
        'user': options.get('user', ''),
        'pwd': options.get('pwd', ''),
    }
    print(conn_params)

connect()                                      # {'host':'127.0.0.1', 'pwd':'', 'user':'', 'port':5432}
connect(host='127.0.0.42', port=5433)          # {'host':'127.0.0.42', 'pwd':'', 'user':'', 'port':5433}
connect(port=5431, user='fab', pwd='gandalf')  # {'host':'127.0.0.1','pwd':'gandalf','user':'fab','port':5431}


# or we can use both at the same time to handle each kind of exceptions
def var_len3(var, *args, **kwargs):
    print(var)
    print(args)
    print(kwargs)
    return

var_len3('Ali', 'a', 2, 5.6, age=23)        # Ali ('a', 5, 5.6) {'age': 23}


# anonymous function ; these functions are not define using def ; lambdas are a one-line version of a function
# syntax    lambda args: expression
add = lambda num1, num2: print(num1+num2)   # takes two arguments and return their sum

add(4, 8)                   # 12


sq = lambda num: num**2     # takes a argument as number and returns its square

print(sq(8))                # 64


# mutable default
# default value of function can be change within the function
# an example of book 'learning python'
def func(a=[], b={}):
    print(a)
    print(b)
    a.append(len(a))        # this will affect a's default value
    b[len(a)] = len(a)      # and this will affect b's one

func()                      # []     {}
func()                      # [0]    {1: 1}
func()                      # [0, 1] {1: 1, 2: 2}


# returning multiple values
# we can return multiple values from function ; in the form of tuple
def moddiv(a, b):
    return a // b, a % b

print(moddiv(20, 7))        # (2, 6)


# Calling function inside a function
def add(lst2):
    total = sum(lst2)
    return total


def average(lst1):
    ave = add(lst1) / (len(lst1))
    return ave

print(average([2, 8, 4, 6, 1]))     # 4.2
