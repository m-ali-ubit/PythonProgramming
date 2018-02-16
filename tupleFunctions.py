
# tuples are immutable objects
# tuple is read-only
# () parenthesis are used for tuple

tuple1 = (1, 2, 3, 4, 5)
tuple2 = ('a', 'b', 'c', 'd')
tuple3 = ('x', 'y', 'z', 6, 7, 8)

# accessing tuples is same as list
print(tuple1[2])    # 3
print(tuple2[3])    # d
print(tuple3[1])    # y

# as we say tuple are read-only so we can not change its elements
# changing elements will raise exceptions

# tuple3[2] = 3   # TypeError
# sort, reverse, insert, pop and remove are also not applicable and raise errors

# Length, concatenation, repetition, membership, iteration, sort, max and min are same as lists
