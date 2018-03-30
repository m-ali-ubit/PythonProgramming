
# selection sort algorithm sorts an array by repeatedly finding the minimum element from unsorted part
# and putting it at the beginning
# Time complexity is n^2

nums = [42, 9, 71, 15, 26, 51, 31, 1, 63]

for n in range(len(nums)):                              # iterate through list
    min_num = n                                         # select n item as minimum
    for m in range(n + 1, len(nums)):                   # iterate through list again but with next item
        if nums[min_num] > nums[m]:                     # if n item is greater than m item
            min_num = m                                 # switch minimum to m item else continue
    nums[n], nums[min_num] = nums[min_num], nums[n]     # after finding least num swap it to the first index

print('Sorted array')
for n in range(len(nums)):
    print('{}'.format(nums[n]), end=' ')
