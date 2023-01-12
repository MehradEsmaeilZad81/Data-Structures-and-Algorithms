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

    def traversePreOrder(self, root: Node):
        if root is None:
            return
        print(root.value, end=" ")
        self.traversePreOrder(root.leftChild)
        self.traversePreOrder(root.rightChild)

    def traverseInOrder(self, root: Node):
        if root is None:
            return
        self.traverseInOrder(root.leftChild)
        print(root.value, end=" ")
        self.traverseInOrder(root.rightChild)

    def traversePostOrder(self, root: Node):
        if root is None:
            return
        self.traversePostOrder(root.leftChild)
        self.traversePostOrder(root.rightChild)
        print(root.value, end=" ")

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
tree.traversePreOrder(tree.root)
print()
tree.traverseInOrder(tree.root)
print()
tree.traversePostOrder(tree.root)
# Output: 5 4 3 2 7 6 8
#         2 3 4 5 6 7 8
#         2 3 4 6 8 7 5
