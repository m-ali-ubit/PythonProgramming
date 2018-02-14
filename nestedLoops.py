
# use of loop inside a loop is called nested loop
# python allow us to do so

# nested for loop
for i in range(1, 6):
    for j in range(1, i + 1):
        print(j, end=' ')
    print()

# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5

s, e = 1, 11
for i in range(s, e, 2):
    for j in range(s-1, int(e/2-i/2)):
        print(" ", end=' ')
    for k in range(s-1, i):
        print(k, end=' ')
    print()

#         0
#       0 1 2
#     0 1 2 3 4
#   0 1 2 3 4 5 6
# 0 1 2 3 4 5 6 7 8

# nested while loop
# prints prime numbers using nested while loop
num = 2
while num < 20:
    x = 2
    while x <= int(num / x):
        if not (num % x):
            break
        x += 1
    if x > int(num / x):
        print(num)
    num += 1

# iterating over multiple sequences
names = ['Ali', 'Umair', 'Zia', 'Ahsan']
fields = ['python', 'iOS', 'Java', 'Oracle']
ages = [23, 23, 23, 22]
# using range
for pos in range(len(names)):
    print(names[pos],
          fields[pos],
          ages[pos])

# using zip
for name, field, age in zip(names, fields, ages):
    print(name, field, age)

# using enumerate
for pos, name in enumerate(names):
    print(name,fields[pos], ages[pos])
