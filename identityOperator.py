
# identity operators compare the memory locations of two objects and returns TRUE or False

x = 10
y = 10
z = 20

print(id(x))    # print the memory location of x
print(id(y))    # print the memory location of y
print(id(z))    # print the memory location of z

print(x is y)       # true because x and y have same memory location as both are 10
print(x is not y)   # false

print(x is z)       # false because x and z have different memory location as x is 10 and z is 20
print(x is not z)   # true

print(y is z)       # false because y and z have different memory location as y is 10 and z is 20
print(y is not z)   # true
