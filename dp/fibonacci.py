from math import floor, log
import numpy as np

# A recursive solution
def fib(n):
    if n <= 0:
        return 0
    if n == 1:
        return 1
    return fib(n-1) + fib(n-2)

# A matrix solution
def fib_matrix_b(n, b):
    '''
    `fib_matrix_b` computes Fibonacci sequence in O(log n) \\
    n is an integer number for fib(n) \\
    b the binary representation of n in a form of 0, 1 sequence
    return a Matrix R
    '''
    M = np.matrix([[1, 1], [1, 0]])
    R = np.matrix([[1, 0], [0, 1]])
    i = floor(log(n, 2))
    while i >= 0:
        if b[i] != 0:
            R = np.matmul(R, M)
        i -= 1
        M = np.matmul(M, M)
        # print(R)
        # print(M)
        # print()
    return R

# to compute
def comp_b(n):
    '''
    `comp_b` computes the binary sequence of n \\
    n is an integer number \\
    return a sequence of 0 and 1
    '''
    L = floor(log(n, 2))
    b = [None for i in range(L+1)]
    i = L
    while i >= 0:
        b[i] = n % 2
        i -= 1
        n = floor(n/2)
        # print(b)
    return b


def fib_matrix(n):
    '''
    `fib_matrix` computes Fibonacci sequence in O(log n) within one pass \\
    n is an integer number for fib(n) \\
    return a Matrix R
    '''
    M = np.matrix([[1, 1], [1, 0]])
    R = np.matrix([[1, 0], [0, 1]])
    L = floor(log(n, 2))
    i = L
    while i >= 0:
        if n % 2 != 0:
            R = np.matmul(R, M)
        i -= 1
        n = floor(n/2)
        M = np.matmul(M, M)
        print(R)
        print(M)
        print()
    return R

def main():
    print(fib(13))
    print(fib_matrix_b(13, [1, 1, 0, 1]))
    print(comp_b(13))
    print(fib_matrix(13))

if __name__ == '__main__':
    main()
    