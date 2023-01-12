class HashTable:
    def __init__(self):
        self.capacity = 5
        self.size = 0
        self.entries = [None] * self.capacity

    class Entry:
        def __init__(self, key: int, value: str):
            self.key = key
            self.value = value

    def put(self, key: int, value: str):
        index = self._hash(key)
        if (self.entries[index] == None):
            self.entries[index] = list()

        bucket = self.entries[index]
        for entry in bucket:
            if (entry.key == key):
                entry.value = value
                return

        bucket.append(self.Entry(key, value))

    def get(self, key: int):
        index = self._hash(key)
        bucket = self.entries[index]
        if bucket:
            for entry in bucket:
                if entry.key == key:
                    return entry.value
        return None

    def _hash(self, key: int):
        return key % self.capacity


# Test
table = HashTable()
table.put(1, "a")
table.put(2, "b")
table.put(3, "c")
table.put(4, "d")
table.put(5, "e")
table.put(6, "f")
print(table.get(1))
# Output: a
