class UnionFind:
    def __init__(self, size):
        self.father = list(range(size))
        self.num_of_sets = size

    def find(self, x):
        if self.father[x] != x:
            self.father[x] = self.find(self.father[x])
        return self.father[x]

    def is_connected(self, x, y):
        return self.find(x) == self.find(y)

    def merge(self, x, y):
        if self.father[self.find(x)] != self.find(y):
            self.father[self.find(x)] = self.find(y)
            self.num_of_sets -= 1