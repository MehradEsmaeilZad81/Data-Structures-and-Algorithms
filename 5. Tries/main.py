class Trie:

    class Node:
        def __init__(self, value: str):
            self.ALPHABET_SIZE = 26
            self.value = value
            self.children = [None] * self.ALPHABET_SIZE
            self.word_finished = False

        def __str__(self):
            return "Node{" + "value=" + self.value + "}"

    def __init__(self):
        self.root = self.Node("")

    def insert(self, word: str):
        node = self.root
        for char in word:
            index = ord(char) - ord('a')
            if not node.children[index]:
                node.children[index] = self.Node(char)
            node = node.children[index]
        node.word_finished = True


# Test
trie = Trie()
trie.insert("hello")
trie.insert("world")
trie.insert("hell")
trie.insert("heaven")
print("Done")
