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
        rnode = self.nodes[label]
        if rnode == None:
            raise Exception("Node not found")
        del self.nodes[label]
        del self.adjacencyList[rnode]
        for node in self.adjacencyList.keys():
            if rnode in self.adjacencyList[node]:
                self.adjacencyList[node].remove(rnode)

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
        print()

    def _traverseDepthFirst(self, root, visited):
        print(root, end=" ")
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

            print(current, end=" ")
            visited.add(current)

            for neighbour in self.adjacencyList[current]:
                if neighbour not in visited:
                    stack.append(neighbour)
        print()

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

            print(current, end=" ")
            visited.add(current)

            for neighbour in self.adjacencyList[current]:
                if neighbour not in visited:
                    queue.append(neighbour)
        print()

    def topologicalSort(self):
        visited = set()
        stack = list()
        for node in self.nodes.values():
            self._topologicalSort(node, visited, stack)

        sorted = list()
        while len(stack) != 0:
            sorted.append(stack.pop().label)

        return sorted

    def _topologicalSort(self, node, visited, stack):
        if node in visited:
            return

        visited.add(node)

        for neighbour in self.adjacencyList[node]:
            self._topologicalSort(neighbour, visited, stack)

        stack.append(node)

    def hasCycle(self):
        all = set()
        for node in self.nodes.values():
            all.add(node)

        visiting = set()
        visited = set()

        while len(all) != 0:
            current = all.pop()
            if self._hasCycle(current, all, visiting, visited):
                return True

        return False

    def _hasCycle(self, node, allnode, visiting, visited):
        allnode.discard(node)
        visiting.add(node)

        for neighbour in self.adjacencyList[node]:
            if neighbour in visited:
                continue
            if neighbour in visiting:
                return True
            if self._hasCycle(neighbour, allnode, visiting, visited):
                return True

        visiting.discard(node)
        visited.add(node)

        return False

    def print(self):
        for node in self.adjacencyList.keys():
            if len(self.adjacencyList[node]) != 0:
                print(node, "is connected to", end=": ")
                for neighbour in self.adjacencyList[node]:
                    print(neighbour, end=" ")
                print()


# graph = Graph()
# graph.addNode("A")
# graph.addNode("B")
# graph.addNode("C")
# graph.addNode("D")
# graph.addEdge("A", "B")
# graph.addEdge("A", "C")
# graph.addEdge("D", "A")
# graph.addEdge("C", "D")
# graph.addEdge("B", "C")
# graph.addEdge("C", "A")
# graph.addEdge("C", "B")
# graph.print()
# graph.BreadthFirstTraversal("C")
# graph.DepthFirstTraversal("C")
# graph.removeEdge("A", "B")
# graph.removeNode("B")
# graph.print()
# graph.BreadthFirstTraversal("C")
# graph.DepthFirstTraversal("C")
# graph.traverseDepthFirst("A")
# graph.traverseDepthFirst(root="G")
# graph.DepthFirstTraversal("A")

# graph = Graph()
# graph.addNode("X")
# graph.addNode("A")
# graph.addNode("B")
# graph.addNode("P")
# graph.addEdge("X", "A")
# graph.addEdge("X", "B")
# graph.addEdge("A", "P")
# graph.addEdge("B", "P")
# list = graph.topologicalSort()
# print(list)

# Test
graph = Graph()
graph.addNode("A")
graph.addNode("B")
graph.addNode("C")
graph.addEdge("A", "B")
graph.addEdge("B", "C")
graph.addEdge("C", "A")
print(graph.hasCycle())
