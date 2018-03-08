
# compare the time complexity of loop, comprehension and generator

from time import time

t = time()      # t saves the current time before the loop

loop = []
for n in range(3000):
    for m in range(n, 3000):
        loop.append((n, m))
print('loop: %.3f sec' % (time() - t))  # elapsed time


t = time()      # t saves the current time before the list comprehension

lst = [(n, m) for n in range(3000) for m in range(n, 3000)]
print('list comprehension: %.3f sec' % (time() - t))  # elapsed time


t = time()      # t saves the current time before the generator expression
generator = list((n, m) for n in range(3000) for m in range(n, 3000))
print('generator expression: %.3f sec' % (time() - t))  # elapsed time

print(loop == lst == generator, len(loop))  # verify that the results are same
print('List Comprehension is the quickest way to make lists')
