
# heap sort is a comparison based sorting technique based on binary heap data structure
# heap sort contain two methods ; heapify build tree and main method heap_sort iterate through indices to sort
# time complexity is O(nLogn)


def heapify(lst, size, i):                           # heapify subtree at index i, size is size of
    largest = i                                      # initialize largest as root
    left = 2*i+1                                     # left is left node of root
    right = 2*i+2                                    # right is right node of root
    if left < size and lst[i] < lst[left]:           # if left child exists and is greater than root
        largest = left
    if right < size and lst[largest] < lst[right]:   # if right child exists and is greater than root
        largest = right
    if largest != i:
        lst[i], lst[largest] = lst[largest], lst[i]  # swap
        heapify(lst, size, largest)                  # heapify the root


def heap_sort(lst):
    size = len(lst)
    for i in range(size, -1, -1):
        heapify(lst, size, i)
    for i in range(size - 1, 0, -1):                 # extracting elements
        lst[i], lst[0] = lst[0], lst[i]              # swap
        heapify(lst, i, 0)

lst = [11, 77, 44, 3, 21, 99, 1, 38]
heap_sort(lst)
print('sorted list')
for i in lst:
    print(i, end=' ')
