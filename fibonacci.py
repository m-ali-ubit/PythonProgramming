
# creating fibonacci series with different methods
# using for loop


def fibonacci1(n):
    a, b = 0, 1
    result = []
    if n <= 1:
        return n
    else:
        for i in range(n):
            if a <= n:
                result.append(a)
                a, b = b, a + b
    return result


print('using for loop')
print(fibonacci1(0))            # [0]
print(fibonacci1(1))            # [0, 1, 1]
print(fibonacci1(30))           # [0, 1, 1, 2, 3, 5, 8, 13, 21]


# using while loop


def fibonacci2(num):
    result = [0]
    next_num = 1
    while next_num <= num:
        result.append(next_num)
        next_num = sum(result[-2:])
    return result

print('using while loop')
print(fibonacci2(0))            # [0]
print(fibonacci2(1))            # [0, 1, 1]
print(fibonacci2(30))           # [0, 1, 1, 2, 3, 5, 8, 13, 21]


# using while and yield


def fibonacci3(num):
    yield 0
    if num == 0:
        return
    a = 0
    b = 1
    while b <= num:
        yield b
        a, b = b, a + b

print('using for while and yield')
print(list(fibonacci3(0)))       # [0]
print(list(fibonacci3(1)))       # [0, 1, 1]
print(list(fibonacci3(30)))      # [0, 1, 1, 2, 3, 5, 8, 13, 21]


def fibonacci4(num):
    a, b = 0, 1
    while a <= num:
        yield a
        a, b = b, a + b

print('using for while loop and yield ; simplified')
print(list(fibonacci4(0)))       # [0]
print(list(fibonacci4(1)))       # [0, 1, 1]
print(list(fibonacci4(30)))      # [0, 1, 1, 2, 3, 5, 8, 13, 21]

# using recursion   ;    function calls itself one or more times in its body

print('using recursion')


def fibonacci5(n):
    if n <= 1:
        return n
    else:
        return fibonacci5(n - 1) + fibonacci5(n - 2)
result = []
for i in range(10):
    result.append(fibonacci5(i))
print(result)
