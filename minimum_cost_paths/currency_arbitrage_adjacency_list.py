# It is a variant of Bellman-Ford problem
# We can regard R_{i, j} as cost of edge(i, j)
# And also re-define paths as rates (use multiplication instead of addition)

# The following class Graph is adapted by https://www.geeksforgeeks.org/bellman-ford-algorithm-dp-23/

class Graph:
    def __init__(self, vertices):
        self.V = vertices # No. of vertices
        self.graph = []   # Use Adjacency list to store the matrix R
 
    # function to add an edge to graph
    def addEdge(self, u, v, w):
        self.graph.append([u, v, w])
         
    # utility function used to print the solution
    def printArr(self, dist):
        print("Vertex Distance from Source")
        for i in range(self.V):
            print("{0}\t\t{1}".format(i, dist[i]))
     
    # The main function that finds shortest distances from src to
    # all other vertices using Bellman-Ford algorithm. The function
    # also detects negative weight cycle
    def BellmanFord(self, src):
 
        # Step 1: Initialize distances from src to all other vertices
        # as INFINITE
        dist = [float("inf")] * self.V
        dist[src] = 1
 
 
        # Step 2: Relax all edges |V| - 1 times. A simple shortest
        # path from src to any other vertex can have at-most |V| - 1
        # edges
        for _ in range(self.V - 1):
            # Update dist value and parent index of the adjacent vertices of
            # the picked vertex. Consider only those vertices which are still in
            # queue
            for u, v, w in self.graph:
                if dist[u] != float("inf") and dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w
 
        # Step 3: check for negative-weight cycles. The above step
        # guarantees shortest distances if graph doesn't contain
        # negative weight cycle. If we get a shorter path, then there
        # is a cycle.
 
        for u, v, w in self.graph:
            if dist[u] != float("inf") and dist[u] + w < dist[v]:
                print("Graph contains negative weight cycle")
                return
                         
        # print all distance
        self.printArr(dist)
    
    # The main function that detects currency arbitrage situation in
    # using adapted Bellman-Ford algorithm
    # with negative cycle detection
    def detect_arbitrage(self):
        # It doesn't matter which node to start
        src = 0
 
        # Step 1: Initialize distances from src to all other vertices
        # as MINUS INFINITE
        dist = [float("-inf")] * self.V
        dist[src] = 1
 
 
        # Step 2: Relax all edges |V| - 1 times. A simple shortest
        # path (largest ratio) from src to any other vertex can have at-most |V| - 1
        # edges
        for _ in range(self.V - 1):
            # Update dist value and parent index of the adjacent vertices of
            # the picked vertex. Consider only those vertices which are still in
            # queue
            for u, v, w in self.graph:
                if dist[u] != float("-inf") and dist[u] * w > dist[v]:
                        dist[v] = dist[u] * w
 
        # Step 3: check for "negative-weight" cycles.
        # The "negative-weight" cycles are the arbitrage situation in our scenario.
        # If we get a larger ratio, then there is a arbitrage situation.
 
        for u, v, w in self.graph:
                if dist[u] != float("-inf") and dist[u] * w > dist[v]:
                    print("Graph contains arbitrage situation")
                    return
                         
        # print all distance
        self.printArr(dist)

g1 = Graph(3)
g1.addEdge(0, 1, 0.5)
g1.addEdge(1, 2, 10)
g1.addEdge(2, 1, 0.21)
 
# Print the solution
g1.detect_arbitrage()

g2 = Graph(3)
g2.addEdge(0, 1, 0.5)
g2.addEdge(0, 2, 4.9)
g2.addEdge(1, 2, 10)
g2.addEdge(1, 0, 1.99)
g2.addEdge(2, 1, 0.09)
g2.addEdge(2, 0, 0.19)

# Print solution
g2.detect_arbitrage()

