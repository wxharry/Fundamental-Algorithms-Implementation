from gettext import find
from os import link
from numpy import size


class Naive_Heuristic_Union:
    pi:list
    n:int

    def __init__(self, n):
        self.n = n
        self.pi = [i for i in range(n+1)]

    def link(self, x, y):
        self.pi[x] = y

    def find(self, x):
        while self.pi[x] != x:
            x = self.pi[x]
        return x

    def union(self, x, y):
        self.link(self.find(x), self.find(y))

class Size_Heuristic_Union:
    pi:list
    n:int
    size:list

    def __init__(self, n):
        self.n = n
        self.pi = [i for i in range(n+1)]
        self.size = [1 for i in range(n+1)]

    def link(self, x, y):
        self.pi[x] = y
        self.size[y] = self.size[x] + self.size[y]

    def find(self, x):
        while self.pi[x] != x:
            x = self.pi[x]
        return x

    def union(self, x, y):
        u = self.find(x)
        v = self.find(y)
        if self.size[u] < self.size[v]:
            self.link(u, v)
        else:
            self.link(v, u)

class Rank_Heuristic_Union:
    pi:list
    rank:list
    n:int

    def __init__(self, n):
        self.n = n
        self.pi = [i for i in range(n+1)]
        self.rank = [0 for i in range(n+1)]

    def link(self, x, y):
        self.pi[x] = y
        self.rank[y] = max(self.rank[y], self.rank[x] + 1)
        
    def find(self, x):
        while self.pi[x] != x:
            x = self.pi[x]
        return x

    def union(self, x, y):
        u = self.find(x)
        v = self.find(y)
        if self.rank[u] < self.rank[v]:
            self.link(u, v)
        else:
            self.link(v, u)

class Path_Compression_Heuristic_Union:
    pi:list
    n:int

    def __init__(self, n):
        self.n = n
        self.pi = [i for i in range(n+1)]

    def link(self, x, y):
        self.pi[x] = y
        
    def find(self, x):
        u = x
        while self.pi[u] != u:
            u = self.pi[u]
        y = self.pi[x]
        while y != u:
            self.pi[x] = u # update to the root
            x = y
            y = self.pi[y]
        return u

    def union(self, x, y):
        self.link(self.find(x), self.find(y))

class Path_Splitting_Heuristic_Union:
    pi:list
    n:int

    def __init__(self, n):
        self.n = n
        self.pi = [i for i in range(n+1)]

    def link(self, x, y):
        self.pi[x] = y
        
    def find(self, x):
        u = x
        while self.pi[u] != u:
            u = self.pi[u]
        y = self.pi[x]
        while y != u:
            self.pi[x] = self.pi[self.pi[x]] # update to its grandparent
            x = y
            y = self.pi[y]
        return u

    def union(self, x, y):
        self.link(self.find(x), self.find(y))

class RankNCompression_Heuristic_Union:
    pi:list
    rank:list
    n:int

    def __init__(self, n):
        self.n = n
        self.pi = [i for i in range(n+1)]
        self.rank = [0 for i in range(n+1)]

    def link(self, x, y):
        self.pi[x] = y
        self.rank[y] = max(self.rank[y], self.rank[x] + 1)
        
    def find(self, x):
        u = x
        while self.pi[u] != u:
            u = self.pi[u]
        y = self.pi[x]
        while y != u:
            self.pi[x] = u # update to the root
            x = y
            y = self.pi[y]
        return u

    def union(self, x, y):
        u = self.find(x)
        v = self.find(y)
        if self.rank[u] < self.rank[v]:
            self.link(u, v)
        else:
            self.link(v, u)


n = 12
print("Naive heuristics")
naive_union = Naive_Heuristic_Union(n)
for i in range(1, n-1, 2):
    naive_union.link(i+1, i)
naive_union.union(4, 8)
naive_union.union(12, 6)
naive_union.union(3, 11)
print("Find(8):",naive_union.find(8))
print(naive_union.pi)
naive_union.union(2, 6)
naive_union.union(10, 11)
print("Find(4):", naive_union.find(4))
print(naive_union.pi)

print("Size heuristics")
size_union = Size_Heuristic_Union(n)
for i in range(1, n-1, 2):
    size_union.union(i, i+1)
size_union.union(4, 8)
size_union.union(12, 6)
size_union.union(3, 11)
print("Find(8):",size_union.find(8))
print(size_union.pi)
print(size_union.size)
size_union.union(2, 6)
size_union.union(10, 11)
print("Find(4):", size_union.find(4))
print(size_union.pi)
print(size_union.size)

print("Rank heuristics")
rank_union = Rank_Heuristic_Union(n)
for i in range(1, n-1, 2):
    rank_union.union(i, i+1)
rank_union.union(4, 8)
rank_union.union(12, 6)
rank_union.union(3, 11)
print("Find(8):",rank_union.find(8))
print(rank_union.pi)
print(rank_union.rank)
rank_union.union(2, 6)
rank_union.union(10, 11)
print("Find(4):", rank_union.find(4))
print(rank_union.pi)
print(rank_union.rank)

print("Only Path Compression heuristics")
path_comp_union = Path_Compression_Heuristic_Union(n)
for i in range(1, n-1, 2):
    path_comp_union.union(i+1, i)
path_comp_union.union(4, 8)
path_comp_union.union(12, 6)
path_comp_union.union(3, 11)
print("Find(8):",path_comp_union.find(8))
print(path_comp_union.pi)
path_comp_union.union(2, 6)
path_comp_union.union(10, 11)
print("Find(4):", path_comp_union.find(4))
print(path_comp_union.pi)

print("Only Path Splitting heuristics")
path_split_union = Path_Splitting_Heuristic_Union(n)
for i in range(1, n-1, 2):
    path_split_union.union(i+1, i)
path_split_union.union(4, 8)
path_split_union.union(12, 6)
path_split_union.union(3, 11)
print("Find(8):",path_split_union.find(8))
print(path_split_union.pi)
path_split_union.union(2, 6)
path_split_union.union(10, 11)
print("Find(4):", path_split_union.find(4))
print(path_split_union.pi)

print("Both Rank and Path Compression heuristics")
rank_compression_union = RankNCompression_Heuristic_Union(n)
for i in range(1, n-1, 2):
    rank_compression_union.union(i, i+1)
rank_compression_union.union(4, 8)
rank_compression_union.union(12, 6)
rank_compression_union.union(3, 11)
print("Find(8):",rank_compression_union.find(8))
print(rank_compression_union.pi)
print(rank_compression_union.rank)
rank_compression_union.union(2, 6)
rank_compression_union.union(10, 11)
print("Find(4):", rank_compression_union.find(4))
print(rank_compression_union.pi)
print(rank_compression_union.rank)
