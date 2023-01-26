class Graph:

    class Node:
        def __init__(self, label):
            self.label = label

        def __str__(self):
            return self.label

    def __init__(self):
        self.nodes = dict()
        self.adjacencyList = dict()

    def addNode(self, label):
        node = self.Node(label)
        self.nodes[label] = node
        self.adjacencyList[node] = list()

    def addEdge(self, label1, label2):
        fromNode = self.nodes[label1]
        toNode = self.nodes[label2]
        if fromNode == None or toNode == None:
            raise Exception("Node not found")
        self.adjacencyList[fromNode].append(toNode)

    def removeNode(self, label):
        node = self.nodes[label]
        if node == None:
            raise Exception("Node not found")
        del self.nodes[label]
        del self.adjacencyList[node]
        for node in self.adjacencyList.keys():
            if node in self.adjacencyList[node]:
                self.adjacencyList[node].remove(node)

    def removeEdge(self, label1, label2):
        fromNode = self.nodes[label1]
        toNode = self.nodes[label2]
        if fromNode == None or toNode == None:
            raise Exception("Node not found")
        self.adjacencyList[fromNode].remove(toNode)

    def traverseDepthFirst(self, root):
        if root not in self.nodes.keys():
            return
        root = self.nodes[root]
        visited = set()
        self._traverseDepthFirst(root, visited)

    def _traverseDepthFirst(self, root, visited):
        print(root)
        visited.add(root)
        for node in self.adjacencyList[root]:
            if node not in visited:
                self._traverseDepthFirst(node, visited)

    def DepthFirstTraversal(self, root):
        if root not in self.nodes.keys():
            return

        visited = set()
        node = self.nodes[root]
        stack = list()
        stack.append(node)

        while len(stack) != 0:
            current = stack.pop()
            if current in visited:
                continue

            print(current)
            visited.add(current)

            for neighbour in self.adjacencyList[current]:
                if neighbour not in visited:
                    stack.append(neighbour)

    def BreadthFirstTraversal(self, root):
        if root not in self.nodes.keys():
            return
        node = self.nodes[root]
        visited = set()
        queue = list()
        queue.append(node)

        while len(queue) != 0:
            current = queue.pop(0)
            if current in visited:
                continue

            print(current)
            visited.add(current)

            for neighbour in self.adjacencyList[current]:
                if neighbour not in visited:
                    queue.append(neighbour)

    def print(self):
        for node in self.adjacencyList.keys():
            if len(self.adjacencyList[node]) != 0:
                print(node, "is connected to", end=": ")
                for neighbour in self.adjacencyList[node]:
                    print(neighbour, end=" ")
                print()


# Test
graph = Graph()
graph.addNode("A")
graph.addNode("B")
graph.addNode("C")
graph.addNode("D")
graph.addEdge("A", "B")
graph.addEdge("A", "C")
graph.addEdge("D", "A")
graph.addEdge("C", "D")
graph.addEdge("B", "C")
graph.print()
graph.BreadthFirstTraversal("C")
graph.removeEdge("A", "B")
graph.removeNode("B")
graph.print()
graph.traverseDepthFirst("A")
graph.traverseDepthFirst(root="G")
graph.DepthFirstTraversal("A")
# Output:
# A is connected to: B C
# B is connected to: C
# C is connected to: D
# D is connected to: A
# C D A B
#
# A is connected to: C
# C is connected to: D
# D is connected to: A
# A C D
# A C D
