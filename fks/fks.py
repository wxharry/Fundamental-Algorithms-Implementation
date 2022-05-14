from math import ceil
import time

K_const = """A, ABOUT, AN, AND, ARE, AS, AT, BE, BOY, BUT, BY, FOR, FROM, HAD, HAVE, HE, HER, HIS, HIM, I, IN, IS, IT, NOT, OF, ON, OR, SHE, THAT, THE, THEY, THIS, TO, WAS, WHAT, WHERE, WHICH, WHY, WITH, YOU"""
K = K_const.split(", ")
n = len(K)
k_global = 1
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

def hash(x, k, n):
    if isinstance(x, str):
        x = adic26(x)
    return ((x*k % p) % n)

bin_dict = dict()
def isGood(k:int)->bool:
    for w in K:
        bin_dict[hash(w, k, n)] = bin_dict.get(hash(w, k, n), []) + [w]
    sum = 0
    for key, lst in bin_dict.items():
        val = len(lst)
        sum += val * (val - 1) / 2
        if sum >= n:
            return False
    return sum < n 

b_array = []
def isPerfect(ki:int, i:int)->bool:
    word_list = bin_dict.get(i)
    if word_list == None:
        return True
    if len(word_list) > b_array[i] * b_array[i]:
        return False
    locations = set()
    for w in word_list:
        loc = hash(w, ki, b_array[i] * b_array[i])
        if loc in locations:
            return False
        else:
            locations.add(loc)
    return True

def showHash():
    # init a hash table
    hash_table = [[] for i in range(n)]
    number_cells = 0
    for key, wl in bin_dict.items():
        i = key
        hash_table[key] = ["" for j in range(b_array[i]*b_array[i])]
        number_cells += b_array[i]*b_array[i]
        for w in wl:
            hash_table[key][hash(w, ks[i], b_array[i] * b_array[i])] = w
    for idx, table in zip(range(len(hash_table)), hash_table):
        print(idx, table)
    print("In my FKS scheme, I used {0} cells".format(number_cells))

maxWord = "ZZZZZ"
print(adic26(maxWord))
p = findPrime(adic26(maxWord))
print("Prime is", p)   # p = 12356633

# pick a good k and display the bins
for k in range(1, p):
    if isGood(k):
        print(str(k) + " is a good k")
        b_array = []
        for i in range(n):
            bi:list = bin_dict.get(i, [])
            b_array.append(len(bi))
            # List all the non-empty Bi's
            if len(bi):
                print("B_{0} = {1}".format(i, bi))
        # show the b[0-39] array
        print("b[] =", b_array)
        break

print()
print("find perfect")
check_point = 0
time_interval = 1
start_time = time.time()
for k in range(1, p):
    try:
        # if check_point == 0 or time.time() - check_point > 60 * time_interval:
        #     print("[Check point]", k)
        #     check_point = time.time()
        bin_dict = {}
        if isGood(k):
            b_array = []
            for i in range(n):
                bi:list = bin_dict.get(i, [])
                b_array.append(len(bi))
            perfect = 0
            ks = [1 for _ in range(n)]
            for i in range(n):
                ki = 1
                while not isPerfect(ki, i):
                    ki += 1
                ks[i] = ki
            k_global = k
            print("Choosing k =", k)
            print("k[] =", ks)
            print("b[] =", b_array)
            showHash()
            break
    except KeyboardInterrupt:
        print(k)
        exit(0)

else:
    print("Failed to find a perfect k")

