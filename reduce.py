
# reduce continually applies the function to the sequence and returns a single value
from functools import reduce

list1 = [2, 11, 5, 13, 6, 21]
print(reduce((lambda x, y: x + y), list1))          # 58

product = reduce((lambda x, y: x * y), list1)
print(product)                                      # 180180
