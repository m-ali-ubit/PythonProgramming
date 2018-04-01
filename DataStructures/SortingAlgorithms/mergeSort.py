
# merge sort follows divide and conquer algorithm
# it divides input array in two halves calls itself for the two halves and then merges the two sorted halves
# time complexity is O(nLogn) for all cases


def merge_sort(lst):
    if len(lst) <= 1:
        return lst
    middle = len(lst) // 2                              # middle index to divide list into halves
    left_list = lst[:middle]                            # left side of list saves to left_list
    right_list = lst[middle:]                           # right side of list saves to right_list
    left_list = merge_sort(left_list)                   # apply recursion on left_list for further division
    right_list = merge_sort(right_list)                 # apply recursion on right_list for further division
    sorted_list = list(merge(left_list, right_list))    # call merge function on divisions and type cast to list
    return sorted_list


def merge(left_half, right_half):                       # merge the sorted halves
    res = []
    while len(left_half) != 0 and len(right_half) != 0:
        if left_half[0] < right_half[0]:
            res.append(left_half[0])
            left_half.remove(left_half[0])
        else:
            res.append(right_half[0])
            right_half.remove(right_half[0])
    if len(left_half) == 0:
        res = res + right_half
    else:
        res = res + left_half
    return res

lst = [11, 77, 44, 3, 21, 99, 1, 38]
print(merge_sort(lst))
