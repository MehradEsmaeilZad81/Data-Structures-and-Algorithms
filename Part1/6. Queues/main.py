class Queue:
    def __init__(self, capacity):
        self._items = [None] * capacity
        self._count = 0
        self._rear = 0
        self._front = 0

    def enqueue(self, item):
        if self._count == len(self._items):
            raise IndexError("Queue is full")
        self._items[self._rear] = item
        self._rear = (self._rear + 1) % len(self._items)
        self._count += 1

    def dequeue(self):
        item = self._items[self._front]
        self._items[self._front] = None
        self._front = (self._front + 1) % len(self._items)
        self._count -= 1
        return item

    def isEmpty(self):
        return self._count == 0

    def __str__(self):
        return str(self._items)


# Test
queue = Queue(5)
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
queue.dequeue()
queue.enqueue(4)
queue.enqueue(5)
queue.enqueue(6)
print(queue.dequeue())
print(queue)
# Output: [6, None, 3, 4, 5]
