'''
Leetcode 50. Pow(x, n)
https://leetcode.com/problems/powx-n/description/
Finish date: 2024-10-02
Algorithm: Math, Recursion
'''

class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        if n < 0:
            return self.myPow(1 / x, -n)
        if n % 2 == 1:
            return x * self.myPow(x, n - 1)
        else:
            m = self.myPow(x, n // 2)
            return m * m
