
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

    def in_order(self, root):                   # left root right traversing
        values = []
        if root:
            values = self.in_order(root.left)
            values.append(root.data)
            values = values + self.in_order(root.right)
        return values

    def pre_order(self, root):                  # root left right traversing
        values = []
        if root:
            values.append(root.data)
            values = values + self.pre_order(root.left)
            values = values + self.pre_order(root.right)
        return values

    def post_order(self, root):                 # left right root traversing
        values = []
        if root:
            values = self.post_order(root.left)
            values = values + self.post_order(root.right)
            values.append(root.data)
        return values

root = Node(5)
root.insert(4)
root.insert(9)
root.insert(2)
root.insert(10)
root.insert(21)
root.insert(6)
root.insert(15)
root.insert(17)

print('in order traversing of tree', root.in_order(root))
print('pre order traversing of tree', root.pre_order(root))
print('post order traversing of tree', root.post_order(root))
