
# exception handling    ;   handle any unexpected error in code and to add debugging capabilities

# try except
#  example 1
x, y = 5, 0
try:                        # operation body    ;   if not successful goes to except body
    z = x / y
except ZeroDivisionError:   # exception body
    print('math error, cannot divide by zero')


# example 2
while True:
    try:
        x = input("enter number: ")
        if x == 'done':
            break
        else:
            x = int(x)
            print(x)
            continue
    except ValueError:
        print("wrong value, enter numbers only")


# multiple except and else
nums = [1, 3, 0, 5, 's', 7, 9]
for num in nums:
    try:
        div = 10/num
    except ZeroDivisionError:
        print('zero cannot be divided')
        continue
    except TypeError:
        print('integer cannot be divided by string')
        continue
    else:
        print('div: {:.4f}'.format(div))


# try finally
nume = [1, 3, 3, 5, 7, 9]
deno = [8, 7, 3, 2, 0, 4]
for nu, de in zip(nume, deno):
    try:
        print('{}/{}'.format(nu, de))
        r = nu / de
    except ZeroDivisionError:
        print('math error, cannot divide by zero')
        continue
    else:
        print('result is: {:.4f}'.format(r))
    finally:
        print('success')


# raise exception
nums = [8, 7, -3, 2, 4, -5]
for num in nums:
    try:
        if num < 0:
            raise ValueError('not a positive number')
        else:
            print(num)
    except ValueError as ve:
            print(ve)
