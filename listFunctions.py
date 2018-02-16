
# initializing lists
list1 = [1, 2, 3, 4, 5]
list2 = ["a", "b", "c", "d"]

# accessing value via index
print(list1[2])             # 3
print(list2[1:3])           # b c

# update list
list1[2] = 6
print(list1[2])             # 3 changed to 6

# deleting item
del list1[2]
print(list1)                # 1 2 4 5  ;  3 is deleted

# list operations
print(len(list1))           # 4
print(len(list2))           # 4

# list concatenation
print(list1 + list2)        # 1 2 4 5 'a' 'b' 'c' 'd'

# list repetition
print(list1 * 2)            # 1 2 4 5 1 2 4 5

# list membership defined in membership.py
# list iteration defined in loops.py
# indexing and slicing is same as string ; see stringFunctions.py

# 2D matrices
# it is actually a list of lists
list3 = [[1, 2, 3, 4], [4, 5, 6, 7], [8, 9, 10, 11]]

print(list3[0][2])          # 3
print(list3[2][1])          # 9

# print all rows
for row in list3:
    print(row)

# we can iterate through it using for nested loop
for row in list3:
    for column in row:
        print(column)

# list methods
# list append
list1.append(6)             # 6 added to list1
print(list1)                # 1 2 4 5 6

# list count ; count the number of occurrence of given item in list
print(list1.count(2))       # 1
list1.append(2)
print(list1.count(2))       # 2

# list index ; returns the very first index of given item
print(list1.index(2))       # 1

# list insert  ; same as append but using insert we can put item on any index
list1.insert(3, 10)         # insert 10 at index 3
print(list1)                # 1 2 4 10 5 6 2

# list pop  ; returns last element of list and removes it
list1.pop()
print(list1)                # 1 2 4 10 5 6

# list remove   ;   delete element from list
list1.remove(5)             # 5 will remove
print(list1)                # 1 2 4 10 6

# list reverse  ;   reveres the order of list
list1.reverse()
print(list1)                # 6 10 4 2 1

# list sort     ;   sort list in ascending order
list1.sort()
print(list1)                # 1 2 4 6 10
list1.sort(reverse=True)    # sort in descending order
print(list1)                # 10 6 4 2 1

# list sorted   ;   the difference b/w sort and sorted is that sorted does not effects the original list
list4 = [9, 1, 5, 7, 3]
print(sorted(list4))        # 1 3 5 7 9
print(list4)                # 9 1 5 7 3
