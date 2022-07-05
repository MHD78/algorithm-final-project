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

    def resultHandler(self, cost,startVertex):
        print(f"cost of shortest path from {startVertex}")
        for key, value in cost.items():
            print(key, ' = ', value)

    def bellmanFord(self, startVertex):
        cost = {i : float("Inf") for i in self.nodes}
        cost[startVertex] = 0

        for i in range(self.V-1):
            for s, d, w in self.graph:
                if cost[s] != float("Inf") and cost[s] + w < cost[d]:
                    cost[d] = cost[s] + w

        self.resultHandler(cost,startVertex)


# test = [[0,0,6,6,0],[3,0,0,0,0],[0,0,0,1,0],[0,1,2,0,0],[0,4,0,2,0]]
stratVertex = int(input("start vertex : "))
matrixRows = int(input("matrix rows : "))
print("input graph matrix : ")
matrix = []
for i in range(matrixRows):    
	single_row = list(map(int, input().split()))  
	matrix.append(single_row)

instance = Graph(matrixRows)
instance.edgeHandler(matrix)
instance.bellmanFord(stratVertex)
