import numpy as np
# X = "AGACGTTCGTTAGCA"
# Y = "CGACTGCTGTATGGA"
X = "abc"
Y = "abcabc"
def levenshteinDistance(s1, s2):
    if len(s1) > len(s2):
        s1, s2 = s2, s1

    distances = range(len(s1) + 1)
    for i2, c2 in enumerate(s2):
        print(distances)
        distances_ = [i2+1]
        for i1, c1 in enumerate(s1):
            if c1 == c2:
                distances_.append(distances[i1])
            else:
                distances_.append(1 + min((distances[i1], distances[i1 + 1], distances_[-1])))
        distances = distances_
    
    return distances[-1]
def edit_distance(word1, word2):
    len_1=len(word1)

    len_2=len(word2)

    x =[[0]*(len_2+1) for _ in range(len_1+1)]#the matrix whose last element ->edit distance

    for i in range(0,len_1+1): #initialization of base case values

        x[i][0]=i
    for j in range(0,len_2+1):

        x[0][j]=j
    for i in range (1,len_1+1):

        for j in range(1,len_2+1):

            if word1[i-1]==word2[j-1]:
                x[i][j] = x[i-1][j-1] 

            else :
                x[i][j]= min(x[i][j-1],x[i-1][j],x[i-1][j-1])+1
    print(np.matrix(x))
    return x[i][j]

# print(edit_distance("Helloworld", "HalloWorld"))
def main():
    print(levenshteinDistance(X, Y))
    print(edit_distance(X, Y))

if __name__ == '__main__':
    main()
    
