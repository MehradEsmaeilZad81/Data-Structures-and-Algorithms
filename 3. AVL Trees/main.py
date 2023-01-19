class AVLTree:
    def __init__(self):
        self.root = None

    class AVLNode:
        def __init__(self, value):
            self.height = 0
            self.value = value
            self.leftChild = None
            self.rightChild = None

        def __str__(self):
            return "Value = " + str(self.value)

    def insert(self, value):
        self.root = self._insert(self.root, value)

    def _insert(self, node, value):
        if node is None:
            return self.AVLNode(value)

        if value < node.value:
            node.leftChild = self._insert(node.leftChild, value)
        else:
            node.rightChild = self._insert(node.rightChild, value)

        node.height = max(self._height(node.leftChild),
                          self._height(node.rightChild)) + 1
        return self.root

    def _height(self, node):
        if node is None:
            return -1
        return node.height

    def __str__(self):
        return str(self.root)


# Test
avl = AVLTree()
avl.insert(10)
avl.insert(20)
avl.insert(30)
print(avl)
