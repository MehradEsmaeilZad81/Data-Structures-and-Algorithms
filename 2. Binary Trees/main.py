class BinaryTree:
    def __init__(self):
        self.root = None

    class Node:
        def __init__(self, value):
            self.value = value
            self.leftChild = None
            self.rightChild = None

        def __str__(self):
            list = []
            if self.leftChild is not None:
                list.insert(0, str((self.leftChild)))
            list.append(self.value)
            if self.rightChild is not None:
                list.append(str(self.rightChild))
            return str(list)

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

    def __str__(self):
        return str(self.root)


tree = BinaryTree()
tree.insert(5)
tree.insert(4)
tree.insert(3)
tree.insert(7)
tree.insert(8)
tree.insert(6)
tree.insert(2)
print(tree)
# Output: [2, 3, [4, 5, [6, 7, 8]]]
