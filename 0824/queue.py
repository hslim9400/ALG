class Queue:

    def __init__(self):
        self.queue = []

    def enqueue(self, data):
        self.queue.append(data)

    def isEmpty(self):
        return not bool(self.queue)

    def dequeue(self):
        if self.isEmpty():
            print('Empty queue')
        else:
            return self.queue.pop(0)

    def peek(self):
        if self.isEmpty():
            print('Empty queue')
        else:
            return self.queue[0]

q = Queue()
q.enqueue(1)
q.enqueue('a')
q.enqueue([1,2,3])
print(q.dequeue())
print(q.dequeue())
print(q.peek())
print(q.dequeue())
q.peek()
q.dequeue()

