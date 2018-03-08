
# generators are kind of iterators
# generator function: they use yield, which allow them to suspend and resume their state between each call


def square():
    for x in range(11):
        yield x ** 2

print(list(square()))       # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
sq = square()
print(next(sq))             # 0
print(next(sq))             # 1
print(next(sq))             # 4
print(next(sq))             # 9
print(next(sq))             # 16
print(next(sq))             # 25
print(next(sq))             # 36
print(next(sq))             # 49
print(next(sq))             # 64
print(next(sq))             # 81
print(next(sq))             # 100
# print(next(sq))           iterator reach its limit at 100 and raise StopIteration error

# yields all terms of the geometric progression a, aq^2, aq^3, ....
# an example from book 'Learning Python'


def geometric_progression(a, q):
    k = 0
    while True:
        result = a * q**k
        if result <= 100000:
            yield result
        else:
            return
        k += 1

print(list(geometric_progression(2, 5)))    # [2, 10, 50, 250, 1250, 6250, 31250]

# to iterate through all values one by one
for n in geometric_progression(2, 5):
    print(n)

# yield from expression


def squares():
    yield from (n ** 2 for n in range(11))

for n in squares():
    print(n)

# generator expression
cubes = [c**3 for c in range(11)]       # simple list
cubes_gen = (c**3 for c in range(11))   # list generated by generator

print(cubes)                            # print list of cubes
print(cubes_gen)                        # print generator object
print(list(cubes_gen))                  # generator exhausted to list
print(list(cubes_gen))                  # cubes_gen object is exhausted above now generator object is empty

# an example from book 'Learning Python'


def adder(*n):
    return sum(n)
s1 = sum(map(lambda n: adder(*n), zip(range(100), range(1, 101))))
s2 = sum(adder(*n) for n in zip(range(100), range(1, 101)))

print(s1)                               # 10000
print(s2)                               # 10000
print(s1 == s2)                         # True  ;   both statements returns same result
