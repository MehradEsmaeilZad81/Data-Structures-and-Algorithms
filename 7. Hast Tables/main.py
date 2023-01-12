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
        if (entries[index] == None):
            entries[index] = list()

        bucket = entries[index]
        for entry in bucket:
            if (entry.key == key):
                entry.value = value
                return

        bucket.append(self.Entry(key, value))

    def _hash(self, key: int):
        return key % self.capacity
