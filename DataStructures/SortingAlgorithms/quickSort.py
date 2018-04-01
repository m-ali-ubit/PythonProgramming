
# quick sort follows divide and conquer first select any element as pivot
# places the pivot element at its correct position in sorted list
# and places all smaller to left of pivot and all greater elements to right of pivot
# time complexity ; worst case is O(n^2) and best case is O(nLogn)


def partition(lst, start, end):                          # the function would perform partitioning on list
    small = start - 1                                    # index of smaller element
    pivot = lst[end]                                     # we select last element as pivot
    for i in range(start, end):                          # iterate through list
        if lst[i] <= pivot:                              # if current element is smaller or equal to pivot
            small = small + 1                            # increment index of smaller element
            lst[small], lst[i] = lst[i], lst[small]      # swap the elements
    lst[small + 1], lst[end] = lst[end], lst[small + 1]
    return small + 1


def quick_sort(lst, start, end):
    if start < end:
        pi = partition(lst, start, end)
        quick_sort(lst, start, pi - 1)                   # Separately sort elements before partition
        quick_sort(lst, pi + 1, end)                     # and after partition
