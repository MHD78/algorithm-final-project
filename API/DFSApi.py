from collections import defaultdict

class GraphDFS:
    def __init__(self):
        self.graph = defaultdict(list)
        self.result = []

    def __repr__(self):
        rep = self.graph
        return str(rep)

    # converting inputed matrix data into dictionary
    def edgeHandler(self,matrix):
        for i in range(len(matrix)):
            for j in range(len(matrix)):
                if matrix[i][j] == 1:
                    self.graph[i].append(j)
        

    # A function for chechking all nodes
    def nodeCheck(self, v, visited):

        visited.add(v)
        self.result.append(v)
        for neighbour in self.graph[v]:
            if neighbour not in visited:
                self.nodeCheck(neighbour, visited)

    # recursive DFS traversal for all nodes
    def DFS(self, v):
        visited = set()
        self.nodeCheck(v, visited)

        if len(self.result) == len(self.graph):
            return self.result

