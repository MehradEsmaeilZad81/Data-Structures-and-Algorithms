class Trie:

    class Node:
        def __init__(self, value: str):
            self.value = value
            self.children = dict()
            self.word_finished = False

        def __str__(self):
            return "Node{" + "value=" + self.value + "}"

    def __init__(self):
        self.root = self.Node("")

    def insert(self, word: str):
        node = self.root
        for char in word:
            if not node.children.get(char):
                node.children[char] = self.Node(char)
            node = node.children.get(char)
        node.word_finished = True


# Test
trie = Trie()
trie.insert("hello")
trie.insert("world")
trie.insert("hell")
trie.insert("heaven")
print("Done")
