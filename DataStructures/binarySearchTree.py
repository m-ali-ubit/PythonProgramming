
class Node:

    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    def insert(self, new_data):                  # method to insert node in tree
        if self.data:
            if new_data < self.data:             # compare new node data with current node data
                if self.left is None:            # if new_data less than current goes to left
                    self.left = Node(new_data)
                else:
                    self.left.insert(new_data)
            elif new_data > self.data:           # else goes to right
                if self.right is None:
                    self.right = Node(new_data)  # we apply recursion to traverse to deep of tree
                else:
                    self.right.insert(new_data)
        else:
            self.data = new_data

    def print_tree(self):                        # function to print tree
        if self.left:
            self.left.print_tree()
        print(self.data)
        if self.right:
            self.right.print_tree()

    def search(self, key):                      # function to find value in a tree
        if key < self.data:                     # compare if key is less than current node data
            if self.left is None:               # if lest node data is none
                return print(key, 'not found')  # data not found
            return self.left.search(key)        # else apply recursion on left node
        elif key > self.data:                   # else if key is greater than node data check for right node
            if self.right is None:              # if right node is null
                return print(key, 'not found')  # key not found
            return self.right.search(key)       # else apply recursion on right node
        else:
            print(key, 'found')                 # if value found print key found

root = Node(5)
root.insert(4)
root.insert(9)
root.insert(2)
root.insert(10)

root.search(6)              # not found
root.search(9)              # found
root.search(11)             # not found
root.search(2)              # found
