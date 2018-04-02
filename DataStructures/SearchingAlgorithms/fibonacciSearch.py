
# fibonacci search is also works on sorted list
# fibonacci search is a comparison-based technique that uses fibonacci numbers to search
# it follows divide and conquer algorithm but divides given list in unequal parts
# time complexity is O(Logn)


def fibonacci_search(list, size, key):
    fib2 = 0                            # initialize fibonacci numbers
    fib1 = 1
    fibn = fib2 + fib1
    while fibn < size:
        fib2 = fib1
        fib1 = fibn
        fibn = fib2 + fib1
    offset = -1                         # marks the eliminated range from front

    while fibn > 1:
        i = min(offset + fib2, size - 1)
        if list[i] < key:
            fibn = fib1
            fib1 = fib2
            fib2 = fibn - fib1
            offset = i
        elif list[i] > key:
            fibn = fib2
            fib1 = fib1 - fib2
            fib2 = fibn - fib1
        else:
            return i
    if fib1 and list[offset + 1] == key:
        return offset + 1;
    return -1

lst = [4, 9, 13, 25, 37, 41, 52]
key1 = 52                           # key found at index 6
key2 = 9                            # key found at index 1
key3 = 10                           # key not found

fs1 = fibonacci_search(lst, len(lst), key1)
fs2 = fibonacci_search(lst, len(lst), key2)
fs3 = fibonacci_search(lst, len(lst), key3)

if fs1 == -1:
    print('key not found')
else:
    print('key found at index {}'.format(fs1))

if fs2 == -1:
    print('key not found')
else:
    print('key found at index {}'.format(fs2))

if fs3 == -1:
    print('key not found')
else:
    print('key found at index {}'.format(fs3))
