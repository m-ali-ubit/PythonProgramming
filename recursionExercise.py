
# recursive function that returns the sum of the first n integers


def sum_n(n):
    if n == 0:
        return 0
    else:
        return n + sum_n(n-1)

print(sum_n(10))            # 55


# factorial using recursion


def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)

print(factorial(10))        # 3628800


# tower of hanoi using recursion


def hanoi(n, source, helper, target):
    if n > 0:
        # move tower of size n - 1 to helper:
        hanoi(n - 1, source, target, helper)
        # move disk from source peg to target peg
        if source:
            target.append(source.pop())
        # move tower of size n-1 from helper to target
        hanoi(n - 1, helper, source, target)

source = [5, 4, 3, 2, 1]
target = []
helper = []
print('source:', source, 'helper:', helper, 'target:', target)
hanoi(len(source), source, helper, target)
print('source:', source, 'helper:', helper, 'target:', target)


# converting integer to any base


def base_change(n, base):
    string = "0123456789ABCDEF"
    if n < base:
        return string[n]
    else:
        return base_change(n//base, base) + string[n % base]

print(base_change(4235, 2))         # 1000010001011
print(base_change(4235, 8))         # 10213
print(base_change(4235, 10))        # 4235
print(base_change(4235, 16))        # 108B


# calculate the harmonic sum


def harmonic_sum(n):
    if n < 2:
        return 1
    else:
        return 1 / n + (harmonic_sum(n - 1))

print(harmonic_sum(10))             # 2.9289682539682538
print(harmonic_sum(6))              # 2.4499999999999997


# calculate the geometric sum


def geometric_sum(n):
    if n < 0:
        return 0
    else:
        return 1 / (pow(2, n)) + geometric_sum(n - 1)

print(geometric_sum(10))            # 1.9990234375
print(geometric_sum(6))             # 1.984375
