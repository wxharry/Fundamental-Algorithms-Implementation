import numpy as np
# Define a number that is big enough
inf = 65535

def optimal_triangulation(P, n, W):
    '''
    `optimal_triangulation(P:int[], n:int, W:function)->{'A': A:int[int[]], 'K': K:int[int[]]}`
    computes the optimal solution for triangulation \\
    Inputs: \\
        `P` is a sequence of numbers representing a polygon; \\
        `n` is a integer representing the length of `P`; \\
        `W` is a Weight function for `P` \\
    Outputs: \\
        The output is a dictrionary including: \\
        `A` is a regular matrix for the algorithm, the minimum cost is at A[-1][-1]
        `K` is a splitter matrix for tracking the actual optimal triangulation
    '''
    A = [[0]*(n) for i in range(n)]
    # K stores splitter. It updates the k for the minimum
    K = [[0]*(n) for i in range(n)]

    for t in range(n):
        A[t][t] = P[t]

    # initialize solutions
    for t in range(n-1):
        A[t][t+1] = 0

    for t in range(3, n+1):
        for i in range(n-t+1):
            A[i][i+t-1] = inf
            for k in range(i + 1, i + t - 1):
                # For regular cases, updating A[i, i+t-1] is enough for the minimum cost
                A[i][i+t-1] = min(A[i][i+t-1], A[i][k] + W(i, k, i+t-1) + A[k][i+t-1])

                # The following `if` fills matrix K to record information to find out the actual optimal triangulation 
                if A[i][i+t-1] > A[i][k] + W(i, k, i+t-1) + A[k][i+t-1]:
                    K[i][i+t-1] = k
    # print(np.matrix(A))
    # print(np.matrix(K))
    return {'A':A, 'K':K, }

def main():
    P = [4, 1, 3, 2, 2, 3]
    P1 = [2, 1, 4, 1, 2, 3]
    n = len(P)
    W = lambda i, j, k : P[i] + P[j] + P[k]
    W2 = lambda i, j, k : P[i] * P[j] * P[k]
    W3 = lambda i, j, k : abs(P[i] - P[j])+abs(P[i]-P[k])+abs(P[j]-P[k])
    W4 = lambda i, j, k : P[i]*P[i] + P[j]*P[j] + P[k]*P[k]
    A, K = optimal_triangulation(P1, n, W2)['A'], optimal_triangulation(P, n, W)['K']
    print(np.matrix(A))
    print(np.matrix(K))

if __name__ == '__main__':
    main()
    
