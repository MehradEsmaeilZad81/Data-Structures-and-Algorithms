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

        self._setHeight(node=root)

        return self._balance(root)

    def _balance(self, root):
        if self._isLeftHeavy(root):
            if (self._balanceFactor(root._leftChild) < 0):
                root._leftChild = self._rotateLeft(root._leftChild)
            return self._rotateRight(root)
        elif self._isRightHeavy(root):
            if (self._balanceFactor(root._rightChild) > 0):
                root._rightChild = self._rotateRight(root._rightChild)
            return self._rotateLeft(root)

        return root

    def _rotateLeft(self, root):
        newRoot = root._rightChild
        root._rightChild = newRoot._leftChild
        newRoot._leftChild = root

        self._setHeight(node=root)
        self._setHeight(node=newRoot)

        return newRoot

    def _rotateRight(self, root):
        newRoot = root._leftChild
        root._leftChild = newRoot._rightChild
        newRoot._rightChild = root

        self._setHeight(node=root)
        self._setHeight(node=newRoot)

        return newRoot

    def _setHeight(self, node):
        node._height = max(self._height(node._leftChild),
                           self._height(node._rightChild)) + 1

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
tree.insert(30)
tree.insert(20)
print(tree)
