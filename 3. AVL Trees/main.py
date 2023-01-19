class AVLTree:
    def __init__(self):
        self._root = None

    class AVLNode:
        def __init__(self, value):
            self._height = 0
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

        root._height = max(self._height(root._leftChild),
                           self._height(root._rightChild)) + 1

        balanceFactor = self._balanceFactor(root)
        if self._isLeftHeavy(root):
            print("root._value is Left heavy: ", root._value)
        elif self._isRightHeavy(root):
            print("root._value is Right heavy: ", root._value)

        print("root._height: ", root._height, "root._value: ",
              root._value, "balanceFactor: ", balanceFactor)

        return root

    def _isLeftHeavy(self, node):
        return self._balanceFactor(node) > 1

    def _isRightHeavy(self, node):
        return self._balanceFactor(node) < -1

    def _balanceFactor(self, node):
        return self._height(node._leftChild) - self._height(node._rightChild)

    def _height(self, node):
        if node is None:
            return -1
        return node._height


# Test
tree = AVLTree()
tree.insert(10)
tree.insert(20)
tree.insert(30)
print(tree)
