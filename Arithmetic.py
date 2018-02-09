
# addition
add = 1 + 2                 # adding two integers
print(add)                  # 3

add2 = sum([1, 2, 5, 3])    # parse list of integers in sum function ; return sum of them
print(add2)                 # 11

add3 = 2+5j + 5+3j          # adding two complex numbers
print(add3)                 # (7+8j)

add4 = 4+8j + 2             # adding complex and integer
print(add4)                 # (6+8j)

# subtraction
sub = 10 - 5                # subtracting two integers
print(sub)                  # 5
# subtraction of complex numbers is same as addition

# multiplication
mul = 3 * 5
print(mul)                  # 15

# division
div = 15 / 3
print(div)                  # 5.0

# exponent
power = 2**3                # double ** means exponent
print(power)                # 8
print(pow(2, 3))            # 8 ; builtin function pow() do the same faster

# modulus
mod = 10 % 3                # returns the remainder
print(mod)                  # 1

# floor division
floor = 10 // 3
print(floor)                # 3 ; returns the quotient

# divmod
dm = divmod(10, 3)          # divmod() function returns a tuple of floor division and modulus
print(dm)                   # (3, 1)
