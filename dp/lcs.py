import numpy as np
def lcs(X, Y):
    '''
    `lcs(X:string, Y:string)->object` computes the length of LCS of X and Y \\
    Inputs are two strings and it returns L(X, Y) and the computation matrix
    '''
    # find the length of the strings
    m = len(X)
    n = len(Y)
  
    # declaring the array for storing the dp values
    L = [[None]*(n + 1) for i in range(m + 1)]
  
    """Following steps build L[m + 1][n + 1] in bottom up fashion
    Note: L[i][j] contains length of LCS of X[0..i-1]
    and Y[0..j-1]"""
    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0 or j == 0 :
                L[i][j] = 0
            elif X[i-1] == Y[j-1]:
                L[i][j] = L[i-1][j-1]+1
            else:
                L[i][j] = max(L[i-1][j], L[i][j-1])
  
    # L[m][n] contains the length of LCS of X[0..n-1] & Y[0..m-1]
    # print(np.matrix(L))
    return L[-1][-1], L

def lcs_backward(X, Y):
    '''
    `lcs_backward(X:string, Y:string)->object` computes the length of LCS of X and Y backwards(from bottom-right ro top-left) \\
    Inputs are two strings and it returns L(X, Y) and the computation matrix
    '''
    # find the length of the strings
    m = len(X)
    n = len(Y)
  
    # declaring the array for storing the dp values
    L = [[None]*(n + 1) for i in range(m + 1)]
  
    """Following steps build L[m + 1][n + 1] in bottom up fashion
    Note: L[i][j] contains length of LCS of X[0..i-1]
    and Y[0..j-1]"""
    for i in range(m, -1, -1):
        for j in range(n, -1, -1):
            if i == m or j == n :
                L[i][j] = 0
            elif X[i] == Y[j]:
                L[i][j] = L[i+1][j+1]+1
            else:
                L[i][j] = max(L[i+1][j], L[i][j+1])
  
    # L[m][n] contains the length of LCS of X[0..n-1] & Y[0..m-1]
    # print(np.matrix(L))
    return L[0][0], L

def lcs_recursive(X, Y):
    '''
    `lcs_recursive(X:string, Y:string)->string` computes one of the lcs of X and Y recursively \\
    Inputs are two strings and it returns lcs(X, Y) \\
    The main idea is to use the two matrices(forward and backward) to split X, Y into two subproblems and do it recursively \\
    Notice: this implementation could be improved in many ways; I didn't comment some `print` for better understanding
    '''
    print("input: {},{}".format(X, Y))
    L = lcs(X, Y)[1]
    # print(np.matrix(L))
    m = len(X)
    n = len(Y)

    if L[-1][-1] == 0: return ""
    if n == 1 and L[-1][-1] == 1: 
        # print("Y", Y)
        return Y[0]
    # compute i*
    L_back = lcs_backward(X, Y)[1]
    # print(np.matrix(L_back))
    j = n//2
    i_star = 0
    for i in range(m):
        if L[i][j] + L_back[i+1][j+1] > L[i_star][j] + L_back[i_star+1][j+1]:
            i_star = i
    if lcs(X, Y)[0] != lcs(X[:i_star], Y[:j])[0] + lcs_backward(X[i_star:], Y[j:])[0]:
        i_star = m
    print("i_star is", i_star)
    return lcs_recursive(X[:i_star], Y[:j]) + lcs_recursive(X[i_star:], Y[j:])

# Driver program to test the above function
X = "lengthen"
Y = "elongate"
print("Length of LCS is ", lcs("final", "infill")[0])

# print("Lenght of LCS is ", lcs_backward(X, Y)[0][0])

print("lcs is", lcs_recursive(X, Y))