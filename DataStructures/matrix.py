
# matrix is a special case of two dimensional array where each data element is of strictly same size

from numpy import *

# initializing matrix
print('string to matrix')
string = 'abcdefghijklmnop'
print(string)
string = list(string)                    # string to list
print(string)
string_matrix = reshape(string, (4, 4))  # string list to matrix
print(string_matrix)

print('integer list to matrix')
m = range(25)                   # list of 24 digits ; 0 to 24  ;  25 is excluding
print(m)
m = reshape(m, (5, 5))
print(m)

# accessing matrix
print('access specific row and column')
print('3rd row:', m[2])                  # print 3rd row     ; [10 11 12 13 14]
print('3rd column', m[:, 2])             # print 3rd column  ; [ 2  7 12 17 22]

# pre-format matrix
arr = array([[11, 18, 20, 22, 17],
            [29, 11, 18, 21, 18],
            [17, 15, 21, 20, 19],
            [23, 11, 20, 22, 21],
            [16, 18, 17, 23, 22]])

shaped_arr = reshape(arr, (5, 5))
print('reshaping array')
print(shaped_arr)
print('shape of matrix', arr.shape)

# adding row
arr = append(arr, [[22, 12, 15, 13, 11]], 0)
print('adding 6th row')
print(arr)
print('shape of matrix', arr.shape)

# adding column
arr = insert(arr, [5], [[15], [25], [13], [14], [15], [19]], 1)
print('adding 6th column')
print(arr)
print('shape of matrix', arr.shape)

# delete row
arr = delete(arr, [2], 0)
print('delete 3rd row')
print(arr)
print('shape of matrix', arr.shape)

# delete column
arr = delete(arr, [2], 1)
print('delete 3rd column')
print(arr)
print('shape of matrix', arr.shape)

# update specific element
print('update 2nd row 5th column element')
print(arr[1][4])
arr[1][4] = 13
print('value changed from 25 to 13')
print(arr[1][4])
