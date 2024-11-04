class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [1] * n
        self.max_size = 1 

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x]) 
        return self.parent[x]

    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)

        if rootX != rootY:
        
            if self.size[rootX] < self.size[rootY]:
                rootX, rootY = rootY, rootX
            self.parent[rootY] = rootX
            self.size[rootX] += self.size[rootY]
            self.size[rootY] = 0
        
            self.max_size = max(self.max_size, self.size[rootX])

    def get_max_size(self):
        return self.max_size

t = int(input().strip())
results = []

for _ in range(t):
    n, m = map(int, input().split())
    uf = UnionFind(n)

    for __ in range(m):
        a, b = map(int, input().split())
        uf.union(a - 1, b - 1) 


    results.append(uf.get_max_size())

print("\n".join(map(str, results)))
