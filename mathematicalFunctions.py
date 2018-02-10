
import math         # import math library
# python has lots of mathematical functions some common are given
# pi
print(math.pi)      # 3.141592653589793

# Euler's number
print(math.e)       # 2.718281828459045

# circle constant = 2pi
print(math.tau)     # 6.283185307179586

# not a number
print(math.nan)     # nan

print(math.inf)     # positive infinity

# absolute value
print(abs(14))      # 14
print(abs(-22))     # 22

# ceil ; returns the smallest integer not less than x
print(math.ceil(105.35))    # 106
print(math.ceil(-89.24))    # -89

# exponential ; returns the exponential of x
print(math.exp(5))      # 148.4131591025766

# floor ; returns the largest integer not greater than x
print(math.floor(118.69))   # 118
print(math.floor(-76.35))   # -77

# log ; natural logarithm
print(math.log(64))         # 4.1588830833596715
print(math.log(53.25))      # 3.9749978045895347

# log10 ; base 10 logarithm
print(math.log10(64))       # 1.806179973983887
print(math.log10(53.25))    # 1.7263196121107753

# max ; returns largest number of list or tuple
print(max([5, 7, 15, 11, 3, 26]))   # 26
print(max((9, 19, 31, 2, 14)))      # 31

# min ; returns smallest number of list or tuple
print(min([5, 7, 15, 11, 3, 26]))   # 3
print(min((9, 19, 31, 2, 14)))      # 2

# modf ; returns the fractional and integer parts in a tuple
print(math.modf(123.45))    # (0.45000000000000284, 123.0)
print(math.modf(33))        # (0.0, 33.0)

# round ; returns rounded number to n digits from the decimal point by default n is 0
print(round(48.7625))       # 49
print(round(23.4568, 1))    # 23.5
print(round(62.4587, 2))    # 62.46

# sqrt ; returns square root of number
print(math.sqrt(9))         # 3.0
print(math.sqrt(5.5))       # 2.345207879911715
