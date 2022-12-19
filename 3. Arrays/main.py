class Array:
    def __init__(self, size):
        self.size = size
        self._index = 0
        self.Array = [None] * size

    def insert(self, value):
        if self._index == self.size:
            self.Array = self.Array + [None] * self.size

        self.Array[self._index] = value
        self._index += 1

    def remove(self, index):
        if index < 0 or index > self._index:
            raise IndexError("Index out of range")
        for i in range(index, self._index - 1):
            self.Array[i] = self.Array[i + 1]
        self.Array[self._index - 1] = None
        self._index -= 1
        if self.Array[self.size//2] is None:
            self.Array = self.Array[:self.size//2]

    def indexOf(self, value):
        for i in range(self._index):
            if self.Array[i] == value:
                return i
        return -1

    def __str__(self):
        return str(self.Array)


# Test
Array1 = Array(5)
Array1.insert(1)
Array1.insert(2)
Array1.insert(3)
Array1.insert(4)
Array1.insert(5)
Array1.remove(2)
Array1.insert(6)
Array1.insert(7)
Array1.insert(8)
Array1.remove(3)
print(Array1)
print(Array1.indexOf(6))
# Output: [1, 2, 4, 5, 6, 7, 8, None, None, None]
# Output: 3
