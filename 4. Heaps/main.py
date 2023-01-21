class Heap:
    def __init__(self):
        self.items = [None] * 10
        self.size = 0

    def insert(self, value):
        items[self.size] = value
        self.size += 1

        index = size - 1
        parentIndex = self._parent(index)
        while items[index] > items[parentIndex]:
            self._swap(index, parentIndex)
            index = parentIndex
            parentIndex = self._parent(index)

    def _swap(self, index1, index2):
        items[index1], items[index2] = items[index2], items[index1]

    def _parent(self, index):
        return (index - 1) // 2
