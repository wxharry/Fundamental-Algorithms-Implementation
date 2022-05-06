import numpy as np

inf = float("inf")

def floyd_warshall(graph, showSteps=None):
    dist = list(map(lambda i: list(map(lambda j: j, i)), graph))
    v = len(graph)
    for k in range(v):
        if showSteps: display(dist)
        for i in range(v):
            for j in range(v):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
    return dist

def floyd_warshall_second_minimum(graph, showSteps=None):
    dist1 = list(map(lambda i: list(map(lambda j: j, i)), graph))
    dist2 = list(map(lambda i: list(map(lambda j: inf, i)), graph))
    v = len(graph)
    for k in range(v):
        print("k =", k)
        if showSteps:
            print("dist1")
            display(dist1)
            print("dist2")
            display(dist2)
        for i in range(v):
            for j in range(v):
                x = [dist2[i][j], dist1[i][j],
                            dist1[i][k] + dist1[k][j],
                            dist2[i][k] + dist1[k][j],
                            dist1[i][k] + dist2[k][j]]
                x = list(sorted(set(x)))
                dist2[i][j] = x[1] if len(x) > 1 else inf
                dist1[i][j] = min(dist1[i][j], dist1[i][k] + dist1[k][k] + dist1[k][j])
    return dist1, dist2

def display(graph):
    print(np.array(graph))

graph = [[  0,   3,   8, inf,  -4,],
         [inf,   0, inf,   1,   7,],
         [inf,   4,   0, inf, inf,], 
         [  2, inf,  -5,   0, inf,],
         [inf, inf, inf,   6,   0,]]

print("floyd_warshall")
display(floyd_warshall(graph))
print("second minimum cost")
min_st, min_nd = floyd_warshall_second_minimum(graph, True)
display(min_st)
display(min_nd)
