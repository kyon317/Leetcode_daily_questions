class BIT:
    mx = 10 ** 9 + 7
    n = 100
    c = [0] * mx
    a = [0] * mx
    def lowbit(self,x):
        return x & (-x)

    def getsum(self,x):
        ans = 0
        while x > 0:
            ans = ans + self.c[x]
            x = x - self.lowbit(x)
        return ans

    def update(self,x,val):
        self.a[x] += val
        while x <= self.n:
            self.c[x] += val
            x += self.lowbit(x)

    print(lowbit(34))
