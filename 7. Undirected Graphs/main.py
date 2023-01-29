class WeightedGraph:

    class Node:
        def __init__(self, label):
            self.label = label

        def __str__(self):
            return self.label

    class Edge:
        def __init__(self, fromNode, toNode, weight):
            self.fromNode = fromNode
            self.toNode = toNode
            self.weight = weight

        def __str__(self):
            return f"{self.fromNode} -> {self.toNode} ({self.weight})"

    def __init__(self):
        self.nodes = dict()
        self.adjacencyList = dict()

    def addNode(self, label):
        node = self.Node(label)
        self.nodes[label] = node
        self.adjacencyList[node] = list()

    def addEdge(self, label1, label2, weight):
        fromNode = self.nodes[label1]
        toNode = self.nodes[label2]
        if fromNode == None or toNode == None:
            raise Exception("Node not found")
        self.adjacencyList[fromNode].append(
            self.Edge(fromNode, toNode, weight))
        self.adjacencyList[toNode].append(
            self.Edge(toNode, fromNode, weight))

    def getShortestDistance(self, label1, label2):
        fromNode = self.nodes[label1]
        toNode = self.nodes[label2]
        distances = dict()
        for node in self.nodes.values():
            distances[node] = float("inf")
        distances[fromNode] = 0

        visited = set()
        queue = list()
        queue.append(fromNode)
        while len(queue) > 0:
            node = queue.pop(0)
            visited.add(node)
            for edge in self.adjacencyList[node]:
                if edge.toNode in visited:
                    continue
                newDistance = distances[node] + edge.weight
                if newDistance < distances[edge.toNode]:
                    distances[edge.toNode] = newDistance
                queue.append(edge.toNode)

        return distances[toNode]

    def print(self):
        for fromNode, edges in self.adjacencyList.items():
            for edge in edges:
                print(edge)


# Test
graph = WeightedGraph()
graph.addNode("A")
graph.addNode("B")
graph.addNode("C")
graph.addNode("D")

graph.addEdge("A", "B", 10)
graph.addEdge("A", "C", 20)
graph.addEdge("B", "D", 30)
graph.addEdge("C", "D", 40)

graph.print()
print("A --> D",graph.getShortestDistance("A", "D"))
print("A --> B",graph.getShortestDistance("A", "B"))
print("B --> D",graph.getShortestDistance("B", "D"))
print("C --> D",graph.getShortestDistance("C", "D"))
