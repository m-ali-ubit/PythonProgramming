
class Node:                                     # create class which stores data and next element's object
    def __init__(self, data=None):
        self.data = data                        # data variable
        self.next_node = None                   # variable to save next object
        self.prev_node = None


class DoubleLinkedList:                         # save the sequence of nodes
    def __init__(self):
        self.head = None                        # to save the head pointer node
        self.tail = None                        # to save the tail pointer node

    def print_list_from_head(self):             # function to print all node's data from head to tail
        head_node = self.head
        while head_node is not None:
            print(head_node.data)
            head_node = head_node.next_node

    def print_list_from_tail(self):             # function to print all node's data from tail to head
        tail_node = self.tail
        while tail_node is not None:
            print(tail_node.data)
            tail_node = tail_node.prev_node

    def insert_at_start(self, new_data):        # function to insert node at beginning of sequence
        new_node = Node(new_data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            print('node successfully inserted')
            return
        else:
            new_node.next_node = self.head      # assign new_node's next to existing head node
            self.head.prev_node = new_node
            self.head = new_node                # assign head to new_node
            print('node successfully inserted')

    def insert_at_end(self, new_data):          # function to insert node at end of sequence
        new_node = Node(new_data)
        if self.tail is None:
            self.head = new_node
            self.tail = new_node
            print('node successfully inserted')
            return
        else:
            new_node.prev_node = self.tail
            self.tail.next_node = new_node
            self.tail = new_node
            print('node successfully inserted')

    def insert_in_between(self, middle_node,  new_data):  # function to insert node at between of sequence
        if middle_node is None:
            print("Middle node not found")
            return
        new_node = Node(new_data)
        new_node.next_node = middle_node.next_node
        temp_node = middle_node.next_node
        middle_node.next_node = new_node
        temp_node.prev_node = new_node
        new_node.prev_node = middle_node
        print('node successfully inserted')

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
        temp_tail = self.tail
        prev = None
        next_ = None
        if temp_head is None:
            print('sequence is empty, value not found')
            return
        elif temp_head is not None:
            if temp_head.data == key:
                self.head = temp_head.next_node
                temp_head = None
                print('node successfully removed')
                return

            elif temp_tail == key:
                self.tail = temp_tail.prev_node
                temp_tail = None
                print('node successfully removed')
                return

            else:
                while temp_head is not None:
                    if temp_head.data == key:
                        print('node successfully removed')
                        break
                    prev = temp_head
                    temp_head = temp_head.next_node
                    next_ = temp_head.next_node
                prev.next_node = temp_head.next_node
                next_.prev_node = temp_head.prev_node
                temp_head = None
