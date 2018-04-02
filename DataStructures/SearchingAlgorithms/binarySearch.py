
# binary search can only be implement on sorted list
# searches  by repeatedly dividing the search interval in half
# time complexity is O(Logn)


def binary_search(lst, left, right, key):
    if right >= left:                                     # if elements are remaining to be checked
        mid = int(left + (right - left)/2)                     # finds the mid element of list
        if lst[mid] == key:                               # if element is present at the middle
            return mid
        elif lst[mid] > key:                              # if element is smaller than mid go to left sublist
            return binary_search(lst, left, mid-1, key)
        else:
            return binary_search(lst, mid+1, right, key)  # else element is greater than mid go to right sublist
    else:
        return -1                                         # return -1 means key not found

lst = [4, 9, 13, 25, 37, 41, 52]
key1 = 52                           # key found at index 6
key2 = 9                            # key found at index 1
key3 = 10                           # key not found

bs1 = binary_search(lst, 0, len(lst)-1, key1)
bs2 = binary_search(lst, 0, len(lst)-1, key2)
bs3 = binary_search(lst, 0, len(lst)-1, key3)

if bs1 == -1:
    print('key not found')
else:
    print('key found at index {}'.format(bs1))

if bs2 == -1:
    print('key not found')
else:
    print('key found at index {}'.format(bs2))

if bs3 == -1:
    print('key not found')
else:
    print('key found at index {}'.format(bs3))
