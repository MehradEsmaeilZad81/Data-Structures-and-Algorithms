class Trie:

    class Node:
        def __init__(self, value: str):
            self.value = value
            self.children = dict()
            self.word_finished = False

        def __str__(self):
            return "Node{" + "value=" + self.value + "}"

        def hasChild(self, char):
            return char in self.children

        def addChild(self, char):
            node.children[char] = self.Node(char)

        def getChild(self, char):
            return self.children.get(char)

    def __init__(self):
        self.root = self.Node("")

    def insert(self, word: str):
        node = self.root
        for char in word:
            if not node.hasChild(char):
                node.addChild(char)
            node = node.getChild(char)
        node.word_finished = True


# Test
trie = Trie()
trie.insert("hello")
trie.insert("world")
trie.insert("hell")
trie.insert("heaven")
print("Done")
