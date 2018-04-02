
# shell sort starts by sorting pairs of elements far apart from each other
# then progressively reducing the gap between elements to be compared
# time complexity ; worst case O(size^2), best case O(nLogn)


def shell_sort(lst):                                # start with a big gap then reduce the gap
    size = len(lst)
    gap = int(size/2)
    while gap > 0:                                  # keep adding elements until whole list is gap sorted
        for i in range(gap, size):                  # iterate b/w gaps
            temp = lst[i]
            j = i
            while j >= gap and lst[j - gap] > temp:
                lst[j] = lst[j - gap]
                j -= gap
            lst[j] = temp
        gap = int(gap/2)

lst = [11, 77, 44, 3, 21, 99, 1, 38]
shell_sort(lst)
print('sorted list')
for i in lst:
    print(i, end=' ')
