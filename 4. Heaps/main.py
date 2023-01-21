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

    def remove(self):
        if self._isEmpty():
            raise Exception("Heap is empty")

        self.size -= 1
        self.items[0] = self.items[self.size]
        self._bubbleDown()

    def _resize(self):
        newItems = [None] * (len(self.items) * 2)
        for i in range(self.size):
            newItems[i] = self.items[i]
        self.items = newItems

    def _isEmpty(self):
        return self.size == 0

    def _isFull(self):
        return self.size == len(self.items)

    def _bubbleDown(self):
        index = 0
        while (index <= self.size and not self._isValidParent(index)):
            largerChildIndex = self._largerChildIndex(index)
            self._swap(index, largerChildIndex)
            index = largerChildIndex

    def _bubbleUp(self):
        index = self.size - 1
        while index > 0 and self.items[index] > self.items[self._parent(index)]:
            self._swap(index, self._parent(index))
            index = self._parent(index)

    def _swap(self, index1, index2):
        self.items[index1], self.items[index2] = self.items[index2], self.items[index1]

    def _isValidParent(self, index):
        return self.items[index] >= self._leftChild(
            index) and self.items[index] >= self._rightChild(index)

    def _largerChildIndex(self, index):
        if self._leftChild(index) > self._rightChild(index):
            return self._leftChildIndex(index)
        return self._rightChildIndex(index)

    def _rightChild(self, index):
        return self.items[self._rightChildIndex(index)]

    def _leftChild(self, index):
        return self.items[self._leftChildIndex(index)]

    def _rightChildIndex(self, index):
        return index * 2 + 2

    def _leftChildIndex(self, index):
        return index * 2 + 1

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
