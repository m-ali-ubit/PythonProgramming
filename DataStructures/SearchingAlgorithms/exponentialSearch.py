
# exponential search also implement on sorted list
# exponential search consists of two methods, first method determines range of list in which the key might be
# in the second method a binary search is performed on the range
# time complexity is O(Logn)


def binary_search(lst, left, right, key):
    if right >= left:
        mid = int(left + (right - left)/2)
        if lst[mid] == key:
            return mid
        elif lst[mid] > key:
            return binary_search(lst, left, mid-1, key)
        else:
            return binary_search(lst, mid+1, right, key)
    else:
        return -1


def exponential_search(list, size, key):
    if list[0] == key:                      # if key is at index 0
        return 0
    i = 1
    while i < size and list[i] <= key:      # find range for binary search by repeated doubling
        i = i * 2
    return binary_search(list, i / 2, min(i, size), key)

lst = [4, 9, 13, 25, 37, 41, 52]
key1 = 52                           # key found at index 6
key2 = 9                            # key found at index 1
key3 = 10                           # key not found

es1 = exponential_search(lst, len(lst), key1)
es2 = exponential_search(lst, len(lst), key2)
es3 = exponential_search(lst, len(lst), key3)

if es1 == -1:
    print('key not found')
else:
    print('key found at index {}'.format(es1))

if es2 == -1:
    print('key not found')
else:
    print('key found at index {}'.format(es2))

if es3 == -1:
    print('key not found')
else:
    print('key found at index {}'.format(es3))
