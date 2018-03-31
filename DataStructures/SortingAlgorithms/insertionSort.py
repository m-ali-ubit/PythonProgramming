
# insertion sort works by comparing each element to its previous elements if they are greater than switch
# until the selected element reach its correct position
# time complexity is O(n*n)


def insertion_sort(lst):
    for i in range(1, len(lst)):        # iterate through 1 to length of list
        key = lst[i]
        j = i - 1
        while j >= 0 and key < lst[j]:  # iterate till j reach to 0 index and key value is less than j value
            lst[j + 1] = lst[j]         # move elements of list that are greater than key, to one position ahead
            j -= 1
        lst[j + 1] = key                # switch key to next element
    print('Sorted array')
    for i in range(len(lst)):
        print('{}'.format(lst[i]), end=' ')
    print()

lst = [11, 45, 36, 29, 9, 21, 39]

insertion_sort(lst)
