
x = 5       # = assigns values from right operands to left operand
y = 10

z = x + y   # assign z the sum of x and y
print(z)    # 15

i = 2
i += x      # adds right operand to left and assign result to left ; equivalent to i = i + x
print(i)    # value of i changed to 7

j = 20
j -= y      # subtract right operand to left and assign result to left ; equivalent to j = j - y
print(j)    # value of j changed to 10

k = 5
k *= x      # multiply right operand to left and assign result to left ; equivalent to k = k + x
print(k)    # value of k changed to 25

l = 50
l /= y      # divide right operand to left and assign result to left ; equivalent to l = l + y
print(l)    # value of l changed to 5.0

m = 30
m %= x      # take modulus of two values and assign result to left operand ; equivalent to m = m % x
print(m)    # value of m changed to 0

n = 25
n //= y     # perform floor division and assign result to left operand ; equivalent to n = n // y
print(n)    # value of n changed to 2

o = 3
o **= x     # perform exponential on operands and assign result to left ; equivalent to o = o ** x
print(o)    # value of o changed to 243
