
# set is a collection of unordered items
# duplication is not allowed
# elements are immutable ; but as a whole is mutable
# do not support indexing and slicing like lists and tuples

# creating sets
nums = set([1, 2, 3, 4, 5, 6, 7])
string = {'a', 'b', 'c', 'd', 'e'}

print(nums)
print(string)

print(type(nums))
print(type(string))

# as sets are immutable we cannot access any single element but loop through it
for n in nums:
    print(n)                 # 1 2 3 4 5 6 7

for s in string:
    print(s)                 # a b c d e

# adding item
nums.add(8)
print(nums)                  # 8 is added

# removing item
string.discard('e')
print(string)                # e is eliminated

# union of sets
nums2 = {5, 6, 7, 8, 9}
union = nums | nums2         # | is the union symbol
print(union)                 # {1, 2, 3, 4, 5, 6, 7, 8, 9}

# intersection of sets
intersection = nums & nums2  # & is the intersection symbol
print(intersection)          # {8, 5, 6, 7}

# difference of sets
diff1 = nums - nums2         # - symbol of difference for sets
diff2 = nums2 - nums
print(diff1)                 # {1, 2, 3, 4}
print(diff2)                 # {9}

# compare sets  ;   subset or superset
nums3 = {1, 2, 3, 4, 5, 6, 7, 8, 9}
subset1 = nums <= nums3      # nums is the subset of nums3
subset2 = nums2 <= nums3     # nums2 is the subset of nums3
subset3 = nums <= nums2      # nums is the subset of nums2
superset1 = nums3 > nums     # nums3 is the superset of nums
superset2 = nums3 > nums2    # nums3 is the superset of nums2
superset3 = nums2 > nums     # nums2 is the superset of nums

print(subset1)               # True
print(subset2)               # True
print(subset3)               # False
print(superset1)             # True
print(superset2)             # True
print(superset3)             # False
