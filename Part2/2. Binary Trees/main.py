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
        if self.root is None:
            raise Exception("Tree is empty")

        cuurent = self.root
        while cuurent.leftChild is not None:
            cuurent = cuurent.leftChild
        return cuurent.value

    # def _min(self, root: Node):
    #     if root is None:
    #         return
    #     if root.leftChild == None and root.rightChild == None:
    #         return root.value

    #     left = self._min(root.leftChild)
    #     right = self._min(root.rightChild)

    #     if left is None:
    #         return min(right, root.value)
    #     if right is None:
    #         return min(left, root.value)

    #     return min(left, right, root.value)
    def equals(self, other: "BinaryTree"):
        if other is None:
            raise Exception("Other tree is empty")
        return self._equals(self.root, other.root)

    def _equals(self, root1: Node, root2: Node):
        if root1 is None and root2 is None:
            return True
        if root1 is not None and root2 is not None:
            return root1.value == root2.value and self._equals(root1.leftChild, root2.leftChild) and self._equals(root1.rightChild, root2.rightChild)

        return False

    # Just for testing
    def swapRoot(self):
        temp = self.root.leftChild
        self.root.leftChild = self.root.rightChild
        self.root.rightChild = temp

    def isBinarySearchTree(self):
        return self._isBinarySearchTree(self.root, float("-inf"), float("inf"))

    def _isBinarySearchTree(self, root: Node, min: int, max: int):
        if root is None:
            return True
        if root.value < min or root.value > max:
            return False

        return self._isBinarySearchTree(root.leftChild, min, root.value - 1) and self._isBinarySearchTree(root.rightChild, root.value + 1, max)

    def getNodesAtDistance(self, distance: int):
        height = self.height()
        if distance > height:
            raise Exception("Distance is greater than height of the tree")
        self._getNodesAtDistance(self.root, distance)

    def _getNodesAtDistance(self, root: Node, distance: int):
        if root is None:
            return
        if distance == 0:
            print(root.value, end=" ")
            return
        self._getNodesAtDistance(root.leftChild, distance - 1)
        self._getNodesAtDistance(root.rightChild, distance - 1)

    def __str__(self):
        return str(self.root.value)


# Test
tree = BinaryTree()
tree.insert(5)
tree.insert(4)
tree.insert(3)
tree.insert(7)
tree.insert(8)
tree.insert(6)
tree.insert(2)
tree.insert(10)
tree.insert(9)
tree.insert(11)
tree.insert(1)
tree.traversePreOrder()
print()
tree.traverseInOrder()
print()
tree.traversePostOrder()
print()
print(tree.height())
print(tree.min())
tree2 = BinaryTree()
tree2.insert(5)
tree2.insert(4)
tree2.insert(3)
tree2.insert(7)
tree2.insert(8)
tree2.insert(6)
tree2.insert(2)
tree2.insert(10)
tree2.insert(9)
tree2.insert(11)
tree2.insert(1)
print(tree.equals(tree2))
print(tree.isBinarySearchTree())
tree2.swapRoot()
print(tree.equals(tree2))
print(tree2.isBinarySearchTree())
tree.getNodesAtDistance(2)
# Output: 5 4 3 2 1 7 6 8 10 9 11
#         1 2 3 4 5 6 7 8 9 10 11
#         1 2 3 4 6 9 11 10 8 7 5
#         4
#         1
#         True
#         True
#         False
#         False
#         3 6 8
