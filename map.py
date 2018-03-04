
# map returns an iterator that applies function to every item of iterable, yielding the results
# map(function, iterable, ...)

map1 = map(lambda x: x, [1, 2, 3, 4, 5])                # lambda function iterate on every item of list

# map returns an iterator so if we print map it returns object location
print(map1)                                             # <map object at 0x000000000000>

# to print the output of map we need to wrap into list
map2 = list(map(lambda x: x, [1, 2, 3, 4, 5]))          # map wrapping in list
print(map2)                                             # [1, 2, 3, 4, 5]


def sqr(x): return x ** 2

map3 = list(map(sqr, [1, 2, 3, 4, 5]))                  # pass sqr function to map with list
print(map3)                                             # [1, 4, 9, 16, 25]

# we can pass multiple iterator
map4 = list(map(lambda *x: x, [1, 2, 3, 4], 'abcd'))
print(map4)


def addition(x, y): return x+y                          # returns addition of values

map5 = list(map(addition, [1, 2], [3, 4]))              # iterate addition through two lists ; x and y
print(map5)                                             # [3+1, 4+2] = [4, 6]

# we can pass list of functions as a sequence in map


def square(x):
    return x ** 2                                       # returns square


def cube(x):
    return x ** 3                                       # returns cube

f = [square, cube]                                      # list of functions
for num in [1, 2, 3, 4, 5]:
    print(list(map(lambda x: x(num), f)))               # lambda x iterate f push num to each function

# map stops at the shortest iterator
print(list(map(lambda *x: x, [1, 2, 3, 4, 5], 'python', [6, 7, 8])))    # [(1, 'p', 6), (2, 'y', 7), (3, 't', 8)]
# shortest iterator is [6, 7, 8] ; map stops after 3rd iteration
