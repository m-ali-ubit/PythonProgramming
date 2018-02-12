
# for loop
for x in [1, 2, 3, 4]:  # iterating through given list
    print(x)            # 1 2 3 4

for x in range(0, 10):  # range function creates list of given range of number than iterate through it.
    print(x)            # 0 1 2 3 4 5 6 7 8 9 ; 10 is exclude

# while loop
x = 1

while x <= 10:          # while function repeats statements until condition is true
    print(x)            # 1 2 3 4 5 6 7 8 9 10
    x += 1              # += is the increment operator it increments 1 in x in every iteration.

# break statement in loops ; break terminates the loop
# for loop
for l in 'hello world':
    if l == 'r':
        break
    else:
        print(l)        # h e l l o   w o

# while loop
a = 10

while a > 0:
    print(a)            # 10 9 8 7 6
    a -= 1
    if a == 5:
        break

# continue statement in loops ; continue skips the remainder of loop's body and move to next iteration
# for loop
for l in 'hello world':
    if l == 'w':
        continue
    print(l)            # h e l l o   o r l d

# while loop
i = 10

while i > 0:
    i -= 1
    if i == 5:
        continue
    print(i)            # 9 8 7 6 4 3 2 1
