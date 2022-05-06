class linked_list:
    pi:list
    N:list
    n:int

    def __init__(self, n):
        self.n = n
        self.pi = [i for i in range(n+1)]
        self.N = [i for i in range(n+1)]

    def link(self, x, y):
        self.pi[x] = self.N[y]
        self.N[y] = self.N[x]
        self.N[x] = self.pi[x]

    def find(self, x):
        while self.pi[x] != x:
            x = self.pi[x]
        return x

    def union(self, x, y):
        self.link(self.find(x), self.find(y))

class anti_list:
    pi:list
    N:list
    n:int

    def __init__(self, n):
        self.n = n
        self.pi = [i for i in range(n+1)]
        self.N = [i for i in range(n+1)]

    def link(self, x, y):
        # Set all the children pointing to y
        self.pi[x] = y
        _x = x
        x = self.N[x]
        while self.pi[x] != y:
            self.pi[x] = y
            x = self.N[x]
        self.__merge(_x, y)
        self.N[y] = _x

    def __merge(self, x, y):
        if self.N[x] == x and self.N[y] == y:
            return
        elif self.N[x] == x and self.N[y] != y:
            _y = self.find_head(y)
            self.N[_y] = x
            self.N[x] = _y
        elif self.N[x] != x and self.N[y] == y:
            _x = self.find_head(x)
            self.N[_x] = x
        elif self.N[x] != x and self.N[y] != y:
            _x = self.find_head(x)
            self.N[_x] = self.N[y]
            _y = self.find_head(y)
            self.N[_y] = x
        return
    
    def find_head(self, x):
        _x = x
        x = self.N[self.N[x]]
        while self.N[x] != self.N[_x]:
            x = self.N[x]
        return x

    def find(self, x):
        while self.pi[x] != x:
            x = self.pi[x]
        return x
        
    def union(self, x, y):
        self.link(self.find(x), self.find(y))


n = 12
print("linked_list")
ll = linked_list(n)
for i in range(1, n-1, 2):
    ll.link(i+1, i)
ll.union(4, 8)
ll.union(12, 6)
ll.union(3, 11)
print("Find(8):",ll.find(8))
print(ll.pi)
print(ll.N)
ll.union(2, 6)
ll.union(10, 11)
print("Find(4):", ll.find(4))
print(ll.pi)
print(ll.N)


print("anti-list")
al = anti_list(n)
for i in range(1, n-1, 2):
    al.link(i+1, i)
al.union(4, 8)
print(al.pi)
print(al.N)
al.union(12, 6)
print(al.pi)
print(al.N)
al.union(3, 11)
print("Find(8):",al.find(8))
print(al.pi)
print(al.N)
al.union(2, 6)
al.union(10, 11)
print("Find(4):", al.find(4))
print(al.pi)
print(al.N)