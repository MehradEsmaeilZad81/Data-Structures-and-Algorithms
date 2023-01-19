class AVLTree:
    def __init__(self):
        self.root = None

    class AVLNode:
        def __init__(self, value):
            self.height = 0
            self.value = value
            self.leftChild = None
            self.rightChild = None
