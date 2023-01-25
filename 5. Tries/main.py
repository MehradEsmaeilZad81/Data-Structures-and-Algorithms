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

        def getChildren(self):
            return self.children.values()

        def hasChildren(self):
            return len(self.children) > 0

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

    def traverse(self):
        self._traverse(self.root)

    def _traverse(self, root):
        print(root.value)
        for child in root.getChildren():
            self._traverse(child)

    def remove(self, word: str):
        if word is None:
            return
        self._remove(self.root, word, 0)

    def _remove(self, root, word, index):
        if index == len(word):
            root.isEndOfWord = False
            return

        ch = word[index]
        child = root.getChild(ch)
        if child is None:
            return
        self._remove(child, word, index + 1)

        if not child.hasChildren() and not child.isEndOfWord:
            root.children.pop(ch)


# Test
trie = Trie()
trie.insert("car")
trie.insert("care")
trie.remove("car")
print(trie.contains("car"))
print(trie.contains("care"))

# Output: False
#         True
