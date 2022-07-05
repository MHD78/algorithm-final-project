class Graph:
    def __init__(self, vertices):
        self.V = vertices   
        self.graph = []     
        self.nodes = []

    def edgeHandler(self, matrix):
        for i in range(self.V):
            for j in range(self.V):
                if matrix[i][j] != 0:
                    self.nodes.append(i)
                    self.graph.append([i, j, matrix[i][j]])

    def bellmanFord(self, startVertex):
        cost = {i : float("Inf") for i in self.nodes}
        cost[startVertex] = 0

        for i in range(self.V-1):
            for s, d, w in self.graph:
                if cost[s] != float("Inf") and cost[s] + w < cost[d]:
                    cost[d] = cost[s] + w
        return cost