
# According to Python documentation:
# zip(*iterables) returns an iterator of tuples, where the i-th tuple contains the i-th element
# from each of the argument sequences or iterables.

obtainedMarks = [22, 26, 21, 15, 19]
maxMarks = [25, 30, 25, 20, 25]

print(list(zip(obtainedMarks, maxMarks)))   # like map, zip also return iterator and need to cast in list

# example from book 'Learning Python'
a = [5, 9, 2, 4, 7]
b = [3, 7, 1, 9, 2]
c = [6, 8, 0, 5, 3]

maxs = map(lambda n: max(*n), zip(a, b, c))  # list the max values of three sequences
print(list(maxs))                            # [6, 9, 2, 9, 7]
