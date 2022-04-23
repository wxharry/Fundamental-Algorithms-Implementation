
from decimal import DivisionByZero

class Polynominal:
    def __init__(self, n) -> None:
        if isinstance(n, int):
            self.number = n
            self.bit = Polynominal.toBit(n)
        elif isinstance(n, str):
            self.number = Polynominal.toNumber(n)
            self.bit = Polynominal.toBit(self.number)

    @staticmethod
    def toBit(n:int):
        return ("{:0b}".format(n))[::-1]

    @staticmethod
    def toNumber(polynomial):
        r = 0; bit = 0
        for i in polynomial:
            r += (2 ** bit) if i == '1' else 0
            bit += 1
        return r

    def __add__(self, other):
        a = self.bit
        b = other.bit
        if len(a) < len(b):
            a, b = b, a
        r = ""
        for i in range(len(b)):
            r = r + str(eval(a[i] + '+' + b[i])%2)
        r = r + a[len(b):]
        return Polynominal(r)

    def __sub__(self, other):
        a = self.bit
        b = other.bit
        if len(a) < len(b):
            a, b = b, a
        r = ""
        for i in range(len(b)):
            r = r + str(eval(a[i] + '-' + b[i])%2)
        r = r + a[len(b):]
        return Polynominal(r)

    def __mul__(self, other):
        sum = Polynominal(0)
        for i in range(len(other.bit)):
            if other.bit[i] == '1':
                sum = sum + Polynominal('0' * i + self.bit)
        return sum
        

    def __mod__(self, other):
        return self.divide(other)["remainder"]

    def divide(self, other):
        divisor = other
        remainder = self
        quotient = "0"
        l = int()
        while remainder.number > divisor.number :
            quotient = '1' + quotient
            l = len(remainder.bit)
            remainder = remainder + Polynominal('0' * (len(remainder.bit) - len(divisor.bit)) + divisor.bit)
            # print(remainder)
            if l - len(remainder.bit) > 1:
                quotient = (l - len(remainder.bit) - 1) * '0' + quotient
        l = len(self.bit) - len(other.bit) + 1
        return {
            "quotient": Polynominal(quotient[len(quotient)-1-l:-1:]),
            "remainder": remainder}

    def __truediv__(self, other):
        if other.number == 0:
            raise DivisionByZero 
        return self.divide(other)["quotient"]
    
    def __str__(self):
        return self.bit

class GF:
    p:int
    n:int
    I:Polynominal
    elements:Polynominal = []

    def __init__(self, p:int, n:int, I:Polynominal):
        self.p = p
        self.n = n
        self.I = I
        for i in range(p**n):
            self.elements.append(Polynominal(i))

    def DisplayElements(self):
        for item in self.elements:
            print(item.number)

    def mul(self, e1, e2):
        return e1 * e2 % self.I

I = Polynominal("11001")
GF16 = GF(2, 4, I)

for i in range(16):
    for j in range(16):
        x = Polynominal(i); y = Polynominal(j)
        print("{:5}".format("{:04}".format(str(GF16.mul(x, y)))), end=' ')
    print()
    