class Heap:
    def __init__(self):
        self.items = [None] * 10
        self.size = 0

    def insert(self, value):
        if self._isFull():
            self._resize()
        self.items[self.size] = value
        self.size += 1
        self._bubbleUp()

    def _resize(self):
        newItems = [None] * (len(self.items) * 2)
        for i in range(self.size):
            newItems[i] = self.items[i]
        self.items = newItems

    def _isFull(self):
        return self.size == len(self.items)

    def _bubbleUp(self):
        index = self.size - 1
        while index > 0 and self.items[index] > self.items[self._parent(index)]:
            self._swap(index, self._parent(index))
            index = self._parent(index)

    def _swap(self, index1, index2):
        self.items[index1], self.items[index2] = self.items[index2], self.items[index1]

    def _parent(self, index):
        return (index - 1) // 2

    def __str__(self):
        return str(self.items[:self.size])


# Test
heap = Heap()
heap.insert(10)
heap.insert(5)
heap.insert(17)
heap.insert(4)
heap.insert(20)
heap.insert(19)
heap.insert(3)

print(heap)
# Output: [20, 19, 17, 4, 10, 5, 3]
