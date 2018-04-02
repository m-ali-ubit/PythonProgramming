
# interpolation search also works on sorted list like binary search but in a better manner
# interpolation search go to different locations according the value of key being searched
# time complexity is O(LogLogn)


def interpolation_search(lst, size, key):
    low = 0                                                 # low represent left most index
    high = (size - 1)                                       # high represent right most index
    while low <= high and lst[low] <= key <= lst[high]:
        pos = low+int(((float(high-low)/(lst[high]-lst[low]))*(key-lst[low])))  # formula to find position
        if lst[pos] == key:                                 # if key is equals to current element
            return pos
        if lst[pos] < key:                                  # if key is greater key is in upper part
            low = pos + 1
        else:                                               # else key is in lower part
            high = pos - 1
    return -1                                               # return -1 if key not found

lst = [4, 9, 13, 25, 37, 41, 52]
key1 = 52                           # key found at index 6
key2 = 9                            # key found at index 1
key3 = 10                           # key not found

is1 = interpolation_search(lst, len(lst), key1)
is2 = interpolation_search(lst, len(lst), key2)
is3 = interpolation_search(lst, len(lst), key3)

if is1 == -1:
    print('key not found')
else:
    print('key found at index {}'.format(is1))

if is2 == -1:
    print('key not found')
else:
    print('key found at index {}'.format(is2))

if is3 == -1:
    print('key not found')
else:
    print('key found at index {}'.format(is3))
