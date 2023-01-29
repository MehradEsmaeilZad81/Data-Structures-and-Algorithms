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
