
# linked list is a sequence of data elements (nodes) which are connected together

# creation of linked list


class Node:                                 # create class which stores data and next element's object
    def __init__(self, data=None):
        self.data = data                    # data variable
        self.next_node = None               # variable to save next object


class LinkedList:                           # save the sequence of nodes
    def __init__(self):
        self.head = None                    # to save the pointer node

    def print_list(self):                   # function to print all node's data
        head_node = self.head
        while head_node is not None:
            print(head_node.data)
            head_node = head_node.next_node

    def insert_at_start(self, new_data):    # function to insert node at beginning of sequence
        new_node = Node(new_data)
        new_node.next_node = self.head      # assign new_node's next to existing head node
        self.head = new_node                # assign head to new_node
        print('node successfully inserted')

    def insert_at_end(self, new_data):
        new_node = Node(new_data)
        if self.head is None:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next_node:
            last_node = last_node.next_node
        last_node.next_node = new_node

    def insert_in_between(self, middle_node,  new_data):
        if middle_node is None:
            print("Middle node not found")
            return
        new_node = Node(new_data)
        new_node.next_node = middle_node.next_node
        middle_node.next_node = new_node

    def find_node(self, key):
        temp_head = self.head
        while temp_head:
            if temp_head.data == key:
                print('value found')
                return True
            else:
                temp_head = temp_head.next_node
        print('value not found')
        return False

    def remove_node(self, key):
        temp_head = self.head
        prev = None
        if temp_head is not None:
            if temp_head.data == key:
                self.head = temp_head.next_node
                temp_head = None
                print('node successfully removed')
                return
        while temp_head is not None:
            if temp_head.data == key:
                print('node successfully removed')
                break
            prev = temp_head
            temp_head = temp_head.next_node
        if temp_head is None:
            print('value not found')
            return
        prev.next_node = temp_head.next_node
        temp_head = None

# creating objects
lst = LinkedList()                          # linkedlist object
n1 = Node(2)
n2 = Node(3)
n3 = Node(5)
n4 = Node(6)
lst.head = n1                               # lst's head saves starting node n1, which has data 1

# link head node to next node
lst.head.next_node = n2

# link 2nd node to 3rd and so on
n2.next_node = n3
n3.next_node = n4

# traversing linkedlist     ;   using function printlist, we define in LinkedList class
print('printing all node of linkedlist')
lst.print_list()                            # 2 3 5 6

# inserting new node with data 1 at beginning
lst.insert_at_start(1)
print('\nprinting all node of linkedlist after inserting at start')
lst.print_list()                            # printing values after inserting

# inserting new node with data 7 at end
lst.insert_at_end(7)
print('\nprinting all node of linkedlist after inserting at end')
lst.print_list()                            # printing values after inserting

# inserting new node with data 4 at node n2
lst.insert_in_between(n2, 4)
print('\nprinting all node of linkedlist after inserting at n2')
lst.print_list()                            # printing values after inserting

# find value in linkedlist
print('\nfind the value in linkedlist')
lst.find_node(8)                            # print whether value found or not
lst.find_node(6)

# remove node from linkedlist
print('\nremove node from linkedlist')
lst.remove_node(10)                         # print value not found because no node exist with value 10
lst.remove_node(5)                          # node removed having value 5
print('\nprinting all nodes of linkedlist after removing')
lst.print_list()
