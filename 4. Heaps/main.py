class Heap:
    def __init__(self):
        self.items = [None] * 10
        self.size = 0

    def insert(self, value):
        items[self.size] = value
        self.size += 1

        index = size - 1
        parentIndex = (index - 1) // 2
        while items[index] > items[parentIndex]:
            items[index], items[parentIndex] = items[parentIndex], items[index]
            index = parentIndex
            parentIndex = (index - 1) // 2
