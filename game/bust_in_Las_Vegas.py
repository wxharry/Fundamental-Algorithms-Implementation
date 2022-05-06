from scipy.special import comb
import numpy as np
from matplotlib import pyplot as plt

# The idea is from https://zhuanlan.zhihu.com/p/338122560?utm_source=wechat_session&utm_medium=social&utm_oi=1097162531415621632
# I implemented his idea with some of my understanding 
# If this code inspires you somehow, please remember to hit a thumb for the original article! Thank you so much!

def generateNXY(n):
    X = np.arange(n)
    N = (5*X+10)//2
    Y = N - X
    return (N, X, Y)
    
def _comb(N, X, n):
    dp = np.zeros(n)
    dp[0] = 1
    for i in range(1, n):
        tmp = comb(N[i], X[i])
        for j in range(n):
            tmp -= comb(N[i]-N[j], X[i]-X[j]) * dp[j]
        dp[i] = tmp
    return dp


# You can adjust epsilon and trial times to show the result
epsilon = 0.0001
trials = 400
N, X, Y = generateNXY(trials)
dp = _comb(N, X, trials)
results = np.zeros(trials)

lessThanEpsilon = False
idxOfLessThanEpsilon = 0
for i in range(0, trials):
    if not lessThanEpsilon :
        tmp = N[i] * dp[i] * np.power(1/3, X[i]) * np.power(2/3, N[i]-X[i])
        results[i] = results[i-1] + tmp
        if tmp < epsilon:
            idxOfLessThanEpsilon = i
            lessThanEpsilon = True
    else:
        results[i] = results[i-1]

print(idxOfLessThanEpsilon)
print(results[-1])
plt.plot(N, results)
plt.title("Game Bust in Las Vegas")
plt.xlabel("Number of games we played")
plt.ylabel("The expectation of the games we played")
plt.show()


