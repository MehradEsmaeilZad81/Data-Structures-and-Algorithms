class AVLTree:
    def __init__(self):
        self._root = None

    class AVLNode:
        def __init__(self, value):
            self._value = value
            self._leftChild = None
            self._rightChild = None

        def __str__(self):
            return str(self._leftChild, self.value, self._rightChild)

    def __str__(self):
        return str(self._root)
