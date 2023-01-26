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
graph.removeEdge("A", "B")
graph.removeNode("B")
graph.print()
# Output:
# A is connected to: B C
# B is connected to: C
# C is connected to: D
# D is connected to: A
#
# A is connected to: C
# C is connected to: D
# D is connected to: A
