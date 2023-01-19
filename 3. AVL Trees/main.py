class AVLTree:
    def __init__(self):
        self._root = None

    class AVLNode:
        def __init__(self, value):
            self._value = value
            self._leftChild = None
            self._rightChild = None

        def __str__(self):
            return str(self._value)

    def __str__(self):
        return str(self._root)

    def insert(self, value):
        self._root = self._insert(self._root, value)

    def _insert(self, root, value):
        if root is None:
            return self.AVLNode(value)

        if value < root._value:
            root._leftChild = self._insert(root._leftChild, value)
        else:
            root._rightChild = self._insert(root._rightChild, value)

        return root


# Test
tree = AVLTree()
tree.insert(10)
tree.insert(20)
tree.insert(30)
print(tree)
