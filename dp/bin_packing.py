# Time complexity: O(n^2)
def bin_packing(M:int, w:list, showResult:False)->int:
    n = len(w)
    dp = [0 for _ in range(n+1)]
    for i in range(1, n+1):
        W = 0
        B = float("inf")
        for j in range(i,0,-1): # find the min in the previous sequence
            W  += w[j-1]
            if W <= M:
                B = min(B, dp[j-1])
        dp[i] = B + 1

    if showResult: print(dp);print(dp[n])
    return dp[n]

bin_packing(5, [1,2,3,4,-5], True)
