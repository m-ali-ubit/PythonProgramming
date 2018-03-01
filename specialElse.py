
# we can use else with for and while loops
# it gives the ability to handle the situations in which loops body does not work
# if the loop body somehow not executed or the condition does not follow then else body executed

# example from book 'Learning Python'
# in this example for loop found the object and print it

people = [('James', 17), ('Kirk', 9), ('Lars', 13), ('Robert', 18)]
for person, age in people:
    if age >= 18:
        driver = (person, age)
        print(driver)
        break
else:
    print('Driver not found.')

# in this example for loop does not found the object and execute else body

people = [('James', 17), ('Kirk', 9), ('Lars', 13), ('Robert', 8)]
for person, age in people:
    if age >= 18:
        driver = (person, age)
        print(driver)
        break
else:
    print('Driver not found.')
