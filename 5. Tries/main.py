class Trie:
    def __init__(self):
        self.root = Node(" ")

    class Node:
        def __init__(self, value: str):
            self.ALPHABET_SIZE = 26
            self.value = value
            self.children = [None] * ALPHABET_SIZE
            self.word_finished = False

        def __str__(self):
            return "Node{" + "value=" + self.value + "}"
