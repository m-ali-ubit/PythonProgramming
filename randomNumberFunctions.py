
import random

# choice(seq) ; returns random item from given list, tuple or string
print(random.choice([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
print(random.choice((1, 2, 3, 4, 5, 6, 7, 8, 9, 10)))
print(random.choice('hello world'))

# randrange(start, stop, step) ; returns random item between given range
print(random.randrange(0, 20))      # excluding 20
print(random.randrange(0, 20, 2))

# randint(x, y) ; returns random integer
print(random.randint(0, 20))    # including 20

# random() ; returns random float number between 0 and 1
print(random.random())

# shuffle ; shuffle the list ; tuples and strings cannot be shuffled
lst = [1, 2, 3, 5, 6, 7]
random.shuffle(lst)
print(lst)

# uniform(x, y) ; returns random float number between x and y
print(random.uniform(1, 20))    # excluding 20

