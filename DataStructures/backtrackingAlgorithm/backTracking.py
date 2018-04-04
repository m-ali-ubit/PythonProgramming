
# Backtracking is a form of recursion
# it involves choosing only option out of any possibilities
# by choosing an option and backtrack from it
# if reach a state where we conclude that this specific option does not give the required solution
# repeat these steps by going across each available option until we get the desired solution


def permute(lst, s):
    if lst == 1:
        return s
    else:
        return [y + x for y in permute(1, s) for x in permute(lst - 1, s)]

print(permute(1, ['a', 'b', 'c', 'd']))     # ['a', 'b', 'c', 'd']
print(permute(2, ['a', 'b', 'c']))          # ['aa', 'ab', 'ac', 'ba', 'bb', 'bc', 'ca', 'cb', 'cc']
print(permute(3, ['a', 'b']))               # ['aaa', 'aab', 'aba', 'abb', 'baa', 'bab', 'bba', 'bbb']
