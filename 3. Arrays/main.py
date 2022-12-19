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

    def __str__(self):
        return str(self.Array)


# Test
Array1 = Array(5)
Array1.insert(1)
Array1.insert(2)
Array1.insert(3)
Array1.insert(4)
Array1.insert(5)
Array1.insert(6)
print(Array1)
# Output: [1, 2, 3, 4, 5, 6, None, None, None, None]
