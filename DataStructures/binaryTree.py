
# A binary tree is made of nodes, where each node contains a "left" reference, a "right" reference,
# and a data element. The topmost node in the tree is called the root.
# Every node (excluding a root) in a tree is connected by a directed edge from exactly one other node.
# This node is called a parent. On the other hand, each node can be connected to arbitrary number of nodes
# called children. Nodes with no children are called leaves, or external nodes.
# Nodes which are not leaves are called internal nodes. Nodes with the same parent are called siblings.


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

root = Node(5)
root.insert(4)
root.insert(9)
root.insert(2)
root.insert(10)

root.print_tree()
