
# stack is a type of data structure which follows first in first out (FIFO) technique
# functions of adding and removing the elements are PUSH and POP but here pop removes very first element of list


class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, data):
        self.queue.insert(0, data)              # queue.insert to add element
        return print(data, 'successfully inserted')

    def dequeue(self):
        if len(self.queue) <= 0:
            return print('queue is empty')
        else:
            return print('pop element:', self.queue.pop())

    def size_of_queue(self):
        return print('length of queue:', len(self.queue))

    def peek_back(self):                       # peek to see the element at front of queue
        return print('at back', self.queue[0])

    def peek_front(self):                        # peek to see the element at back of queue
        return print('at front', self.queue[len(self.queue)-1])

queue = Queue()                     # queue object created
queue.dequeue()                     # queue is empty
queue.enqueue(4)                    # 4 successfully inserted
queue.enqueue(9)                    # 9 successfully inserted
queue.enqueue(3)                    # 3 successfully inserted
queue.peek_front()                  # at front 4
queue.peek_back()                   # at back 3
queue.size_of_queue()               # length of queue: 3
queue.dequeue()                     # pop element: 4
queue.dequeue()                     # pop element: 9
queue.enqueue(5)                    # 5 successfully inserted
queue.peek_front()                  # at front 3
queue.peek_back()                   # at back 5
queue.size_of_queue()               # length of queue: 2
