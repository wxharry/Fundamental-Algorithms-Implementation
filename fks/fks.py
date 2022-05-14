from math import ceil
import time

K_const = """A, ABOUT, AN, AND, ARE, AS, AT, BE, BOY, BUT, BY, FOR, FROM, HAD, HAVE, HE, HER, HIS, HIM, I, IN, IS, IT, NOT, OF, ON, OR, SHE, THAT, THE, THEY, THIS, TO, WAS, WHAT, WHERE, WHICH, WHY, WITH, YOU"""
K = K_const.split(", ")
n = len(K)
p = 2           # a prime number
B:list          # hash table
b:list

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

def hash(x, k, n):
    if isinstance(x, str):
        x = adic26(x)
    return ((x*k % p) % n)

def get_partition(K, k):
    n = len(K)
    hast_table = [[] for _ in range(n)]
    b_array = []
    for w in K:
        hast_table[hash(w, k, n)].append(w)
    for t in hast_table:
        b_array.append(len(t))
    return hast_table, b_array

def get_collision(B):
    sum = 0
    for bin in B:
        val = len(bin)
        sum += val * (val - 1) // 2
    return sum

def isGood(k:int)->bool:
    hash_table, _ = get_partition(K, k)
    collision = get_collision(hash_table)
    return collision < n

def isPerfect(ki:int, i:int)->bool:
    hash_table, _ = get_partition(B[i], ki)
    collision = get_collision(hash_table)
    return collision == 0

def showHash():
    number_cells = n + 2
    for idx, subtable in zip(range(len(B)), B):
        number_cells += 2 + len(subtable) ** 2
        print(idx, subtable)
    print("{0} cells are used in this FKS schema".format(number_cells))

maxWord = "ZZZZZ"
print(adic26(maxWord))
p = findPrime(adic26(maxWord))
print("Prime is", p)   # p = 12356633

# pick a good k and display the bins
for k in range(1, p):
    if isGood(k):
        print(str(k) + " is a good k")
        B, b = get_partition(K, k)
        showHash()
        # show the b[0-39] array
        print("b[] =", b)
        break

print()
print("find perfect")
for k in range(1, p):
    try:
        if isGood(k):
            B, b = get_partition(K, k)
            ks = [1 for _ in range(n)]
            for i in range(n):
                ki = 1
                while not isPerfect(ki, i):
                    ki += 1
                ks[i] = ki
            print("Choosing k =", k)
            print("k[] =", ks)
            print("b[] =", b)
            # showHash()
            break
    except KeyboardInterrupt:
        print(k)
        exit(0)

else:
    print("Failed to find a perfect k")

