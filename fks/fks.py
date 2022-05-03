from math import ceil

K_const = """A, ABOUT, AN, AND, ARE, AS, AT, BE, BOY, BUT, BY, FOR, FROM, HAD, HAVE, HE, HER, HIS, HIM, I, IN, IS, IT, NOT, OF, ON, OR, SHE, THAT, THE, THEY, THIS, TO, WAS, WHAT, WHERE, WHICH, WHY, WITH, YOU"""
K = K_const.split(", ")
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

# TODO: implement function isGood()
def isGood(k:int)->bool:
    pass
    

maxWord = K[0]
for word in K:
    if adic26(maxWord) < adic26(word):
        maxWord = word
print(maxWord, adic26(maxWord))     # WHICH 10657226
p = findPrime(adic26(maxWord))
print(p)   # p = 10657247
