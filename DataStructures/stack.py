
# stack is a type of data structure which follows last in first out (LIFO) technique
# functions of adding and removing the elements are PUSH and POP


class Stack:
    def __init__(self):
        self.stack = []

    def push_(self, data):
        self.stack.append(data)         # list.append used to add element
        return print(data,'successfully added')

    def peek_bottom(self):                     # peek to see the element at top of the stack
        return print('at bottom', self.stack[0])

    def peek_top(self):
        return print('at top', self.stack[len(self.stack)-1])

    def pop_(self):                      # pop method used to remove element from top
        if len(self.stack) <= 0:
            return print('stack is empty')
        else:
            return print('pop element:', self.stack.pop())

stack = Stack()             # create stack object
stack.push_(8)              # 8 successfully added
stack.push_(4)              # 4 successfully added
stack.push_(3)              # 3 successfully added
stack.peek_top()            # at top 3
stack.peek_bottom()         # at bottom 8
stack.push_(1)              # 1 successfully added
stack.peek_top()            # at top 1
stack.peek_bottom()         # at bottom 8
stack.pop_()                # pop element: 1
stack.peek_top()            # at top 3
stack.peek_bottom()         # at bottom 8
stack.pop_()                # pop element: 3
stack.peek_top()            # at top 4
stack.peek_bottom()         # at bottom 8
stack.push_(10)             # 10 successfully added
stack.peek_top()            # at top 10
stack.peek_bottom()         # at bottom 8
stack.pop_()                # pop element: 10
stack.pop_()                # pop element: 4
stack.pop_()                # pop element: 8
stack.pop_()                # stack is empty
