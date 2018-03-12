
# nodes stores data along with the address of the next location of data element
# nodes are used to handle linked lists and tress

# creating nodes


class Integers:                         # create class which stores data and next element's object
    def __init__(self, integer=None):
        self.integer = integer          # data variable
        self.next_integer = None        # variable to save next object

# creating objects
n1 = Integers(1)
n2 = Integers(2)
n3 = Integers(3)
n4 = Integers(4)
n5 = Integers(5)

# assigning object's pointer variable to another object
n1.next_integer = n2                    # object n1 stores next object n2
n2.next_integer = n3                    # object n2 stores next object n3
n3.next_integer = n4                    # object n3 stores next object n4
n4.next_integer = n5                    # object n4 stores next object n5

# traversing through each node
this = n1

while this:
    print(this.integer)
    this = this.next_integer
