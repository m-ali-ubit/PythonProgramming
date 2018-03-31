
# bubble sort algorithm works by repeatedly swapping the adjacent elements if they are in wrong order
# time complexity: worst/average case O(n^n), best case O(n) [it happens only if list already sorted]


def bubble_sort(lst):
    for m in range(len(lst)):                           # iterate through list
        flag = False
        for n in range(0, len(lst)-m-1):                # iterate through list again but with next item
            if lst[n] > lst[n+1]:                       # if item n is greater than its next item
                lst[n], lst[n+1] = lst[n+1], lst[n]     # swap them
                flag = True                             # set flag to true
        if flag is False:                               # the flag is used to check if items are already sorted
            break
    print('Sorted array')
    for i in range(len(lst)):
        print('{}'.format(lst[i]), end=' ')
    print()
lst1 = [1, 2, 3, 4, 5, 6, 7]
lst2 = [11, 45, 36, 29, 9, 21, 39]

bubble_sort(lst1)
bubble_sort(lst2)
