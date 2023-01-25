class Trie:

    class Node:
        def __init__(self, value: str):
            self.value = value
            self.children = dict()
            self.isEndOfWord = False

        def __str__(self):
            return "Node{" + "value=" + self.value + "}"

        def hasChild(self, char):
            return char in self.children

        def getChild(self, char):
            return self.children.get(char)

    def __init__(self):
        self.root = self.Node("")

    def insert(self, word: str):
        node = self.root
        for char in word:
            if not node.hasChild(char):
                node.children[char] = self.Node(char)
            node = node.getChild(char)
        node.isEndOfWord = True

    def contains(self, word: str):
        if word is None:
            return False
        node = self.root
        for char in word:
            if not node.hasChild(char):
                return False
            node = node.getChild(char)
        return node.isEndOfWord


        # Test
trie = Trie()
trie.insert("hello")
trie.insert("world")
trie.insert("hell")
trie.insert("heaven")
print(trie.contains("hel"))
print("Done")
