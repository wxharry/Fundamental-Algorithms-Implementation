# It is a variant of Bellman-Ford problem
# We can regard R_{i, j} as cost of edge(i, j)
# And also re-define paths as rates (use multiplication instead of addition)

# The following class Graph is adapted by https://www.geeksforgeeks.org/bellman-ford-algorithm-dp-23/

class Graph:
    def __init__(self, n):
        self.V = n # No. of vertices
        self.graph = [[1 for _ in range(n)] for _ in range(n)]   # Use Adjacency list to store the matrix R
 
    # function to add an edge to graph
    def addEdge(self, u, v, w):
        self.graph[u][v] = w
         
    # utility function used to print the solution
    def printArr(self, dist):
        print("Vertex Distance from Source")
        for i in range(self.V):
            print("{0}\t\t{1}".format(i, dist[i]))
    
    # The main function that detects currency arbitrage situation in
    # using adapted Bellman-Ford algorithm
    # without negative cycle detection
    def exit_arbitrage(self, src):
 
        # Step 1: Initialize distances from src to all other vertices
        # as MINUS INFINITE
        dist = [float("-inf")] * self.V
        dist[src] = 1
        edges = [(x, y) for x in range(self.V) for y in range(self.V) if self.graph[x][y] != float("inf")]
 
 
        # Step 2: Relax all edges |V| times. A simple shortest
        # path (largest ratio) from src to any other vertex can have at-most |V| - 1 edges
        # After that if there exists an update, there is an arbitrage situation
        for i in range(self.V):
            # Update dist value and parent index of the adjacent vertices of
            # the picked vertex. Consider only those vertices which are still in
            # queue
            for u, v in edges:
                w = self.graph[u][v]
                if dist[u] != float("-inf") and dist[u] * w > dist[v]:
                    if i == self.V - 1:
                        return True
                    dist[v] = dist[u] * w
        return False


    def detect_arbitrage(self):
        if self.exit_arbitrage(0):
            print("Exist arbitrage situation!")
        else:
            print("Free of arbitrage situation!")


g1 = Graph(3)
g1.addEdge(0, 1, 0.5)
g1.addEdge(1, 0, 2)
g1.addEdge(1, 2, 10)
g1.addEdge(2, 1, 0.21)
g1.addEdge(0, 2, 4)
g1.addEdge(2, 1, 0.25)
g1.detect_arbitrage()

g2 = Graph(3)
g2.addEdge(0, 1, 0.5)
g2.addEdge(0, 2, 4.9)
g2.addEdge(1, 2, 10)
g2.addEdge(1, 0, 1.99)
g2.addEdge(2, 1, 0.09)
# g2.addEdge(2, 0, 0.19)
g2.addEdge(2, 0, float("inf"))
g2.detect_arbitrage()

g3 = Graph(3)
g3.addEdge(0, 1, 0.5)
g3.addEdge(1, 0, float("inf"))
g3.addEdge(1, 2, 0.25)
g3.addEdge(2, 1, 4)
g3.addEdge(0, 2, 0.1)
g3.addEdge(2, 0, float("inf"))
g3.detect_arbitrage()
