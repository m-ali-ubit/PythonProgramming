
# there are several searching algorithms
# linear is the simplest one
# complexity of linear search is O(n)


def linear_search(values, key):
    flag = False
    for k in values:
        if k == key:
            print(key, 'value found')
            flag = True
            break
        else:
            continue
    if flag is False:
        print('value not found')

lst = [5, 7, 3, 1, 9, 11, 44, 2, 33, 14, 19, 16, 12]
linear_search(lst, 33)
linear_search(lst, 40)
