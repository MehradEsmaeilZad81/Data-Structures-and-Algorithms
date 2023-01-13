class BinaryTree:
    def __init__(self):
        self.root = None

    class Node:
        def __init__(self, value):
            self.value = value
            self.leftChild = None
            self.rightChild = None

    def insert(self, value: int):
        if self.root is None:
            self.root = self.Node(value)
            return
        else:
            current = self.root
            while True:
                if value < current.value:
                    if current.leftChild is None:
                        current.leftChild = self.Node(value)
                        return
                    else:
                        current = current.leftChild
                elif value > current.value:
                    if current.rightChild is None:
                        current.rightChild = self.Node(value)
                        return
                    else:
                        current = current.rightChild
                else:
                    return

    def find(self, value: int):
        current = self.root
        while current is not None:
            if value < current.value:
                current = current.leftChild
            elif value > current.value:
                current = current.rightChild
            else:
                return True
        return False

    def traversePreOrder(self):
        self._traversePreOrder(self.root)

    def _traversePreOrder(self, root: Node):
        if root is None:
            return
        print(root.value, end=" ")
        self._traversePreOrder(root.leftChild)
        self._traversePreOrder(root.rightChild)

    def traverseInOrder(self):
        self._traverseInOrder(self.root)

    def _traverseInOrder(self, root: Node):
        if root is None:
            return
        self._traverseInOrder(root.leftChild)
        print(root.value, end=" ")
        self._traverseInOrder(root.rightChild)

    def traversePostOrder(self):
        self._traversePostOrder(self.root)

    def _traversePostOrder(self, root: Node):
        if root is None:
            return
        self._traversePostOrder(root.leftChild)
        self._traversePostOrder(root.rightChild)
        print(root.value, end=" ")

    def height(self):
        return self._height(self.root)

    def _height(self, root: Node):
        if root is None:
            return -1
        if root.leftChild == None and root.rightChild == None:
            return 0

        return 1 + max(self._height(root.leftChild), self._height(root.rightChild))

    def min(self):
        return self._min(self.root)

    def _min(self, root: Node):
        if root is None:
            return
        if root.leftChild == None and root.rightChild == None:
            return root.value

        left = self._min(root.leftChild)
        right = self._min(root.rightChild)

        if left is None:
            return min(right, root.value)
        if right is None:
            return min(left, root.value)

        return min(left, right, root.value)

    def __str__(self):
        return str(self.root.value)


tree = BinaryTree()
tree.insert(5)
tree.insert(4)
tree.insert(3)
tree.insert(7)
tree.insert(8)
tree.insert(6)
tree.insert(2)
tree.traversePreOrder()
print()
tree.traverseInOrder()
print()
tree.traversePostOrder()
print()
print(tree.height())
print(tree.min())
# Output: 5 4 3 2 7 6 8
#         2 3 4 5 6 7 8
#         2 3 4 6 8 7 5
#         3
#         2
