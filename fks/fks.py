from email.policy import default
from math import ceil

from attr import has
from numpy import empty

K_const = """A, ABOUT, AN, AND, ARE, AS, AT, BE, BOY, BUT, BY, FOR, FROM, HAD, HAVE, HE, HER, HIS, HIM, I, IN, IS, IT, NOT, OF, ON, OR, SHE, THAT, THE, THEY, THIS, TO, WAS, WHAT, WHERE, WHICH, WHY, WITH, YOU"""
K = K_const.split(", ")
n = len(K)
p = 2

def adic26(word:str)->int:
    bit = 0
    sum = 0
    for ch in word.lower()[::-1]:
        sum += (ord(ch) - ord('a') + 1) * pow(26, bit)
        bit += 1
    return sum


def findPrime(n:int)->int:
    found = False
    while not found:
        n += 1;
        for i in range(2, ceil(pow(n, 0.5))):
            if n % i == 0:
                break
        else:
            found = True
    return n;

def hash(x, k):
    if isinstance(x, str):
        x = adic26(x)
    return ((x*k % p) % n)
    
def isGood(k:int)->bool:
    bin_dict = dict()
    for w in K:
        bin_dict[hash(w, k)] = bin_dict.get(hash(w, k), 0) + 1
    sum = 0
    for key, val in bin_dict.items():
        sum += val * (val - 1) / 2
        if sum >= n:
            return False
    return sum < n 


maxWord = K[0]
for word in K:
    if adic26(maxWord) < adic26(word):
        maxWord = word
print(maxWord, adic26(maxWord))     # WHICH 10657226
p = findPrime(adic26(maxWord))
print("Prime is", p)   # p = 10657247

# pick a good k and display the bins
for k in range(p):
    if isGood(k):
        print(str(k) + " is a good k")
        bin_dict = dict()
        # Collection bins
        for w in K:
            bin_dict[hash(w, k)] = bin_dict.get(hash(w, k), []) + [w]
        
        b_array = []
        for i in range(n):
            bi:list = bin_dict.get(i, [])
            b_array.append(len(bi))
            # List all the non-empty Bi's
            if len(bi):
                print("B_{0} = {1}".format(i, bi))
        # show the b[0-39] array
        print(b_array)
        break



