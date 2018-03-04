
# according to documentation
# filter construct an iterator from those elements of iterable for which function returns True

list1 = [9, 7, 2, 3, 1, 4, 6, 11, 17]
print(list(filter(lambda x: x > 5, list1)))         # [9, 7, 6, 11, 17]

list2 = [2, 4, 5, 6, 9, 12, 15, 16]
print(list(filter(lambda x: x % 2, list2)))         # [5, 9, 15]

list3 = [2, 4, 5, 6, 9, 12, 15, 16]
print(list(filter(lambda x: x % 2 == 0, list3)))    # [2, 4, 6, 12, 16]
