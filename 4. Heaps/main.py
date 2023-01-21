class Heap:
    def __init__(self):
        self.items = [None] * 10
        self.size = 0

    def insert(self, value):
        items[self.size] = value
        self.size += 1
        self._bubbleUp()

    def _bubbleUp(self):
        index = size - 1
        while index > 0 and items[index] > items[self._parent(index)]:
            self._swap(index, self._parent(index))
            index = self._parent(index)

    def _swap(self, index1, index2):
        items[index1], items[index2] = items[index2], items[index1]

    def _parent(self, index):
        return (index - 1) // 2
