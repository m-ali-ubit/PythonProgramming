
# decorator is a function that takes another function and
# extends the behavior of the latter function without explicitly modifying it

from time import sleep, time
from functools import wraps


def measure1(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        t = time()
        func(*args, **kwargs)
        print(func.__name__, 'took:', time() - t)
    return wrapper

@measure1
def f(sleep_time=0.1):
    sleep(sleep_time)
f(sleep_time=0.5)  # f took: 0.5000066757202148


# using two decorators  ;   example from book 'learning python'


def measure2(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        t = time()
        result = func(*args, **kwargs)
        print(func.__name__, 'took:', time() - t)
        return result
    return wrapper


def max_result(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        if result > 100:
            print('Result is too big ({0}). Max allowed is 100.'.format(result))
        return result
    return wrapper


@measure2
@max_result
def cube(n):
    return n ** 3

print(cube(2))          # 8
print(cube(4))          # 216


# decorator factory: decorating a function with a decorator that takes arguments


def max_result(threshold):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            if result > threshold:
                print('Result is too big ({0}). Max allowed is {1}.'.format(result, threshold))
            return result
        return wrapper
    return decorator


@max_result(400)
def square(n):
    return n ** 2


@max_result(250)
def cube(n):
    return n ** 3


@max_result(1000)
def multiply(a, b):
    return a * b


print('square:', square(15))
print('cube', cube(8))
print('multiply', multiply(9, 13))
