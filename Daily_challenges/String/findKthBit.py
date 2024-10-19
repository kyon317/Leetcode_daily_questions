"""
Leetcode 1545. Find Kth Bit in Nth Binary String
https://leetcode.com/problems/find-kth-bit-in-nth-binary-string/description/
Finish date: 2024-10-19
Algorithm: Simulation, Recursion
"""

class Solution:
    "Recursion"
    def findKthBit(self, n: int, k: int) -> str:
        if k == 1:
            return '0'
        mid = 1 << (n - 1)
        if k == mid:
            return '1'
        if k < mid:
            return self.findKthBit(n - 1, k)
        k = mid * 2 - k
        return '0' if self.findKthBit(n - 1, k) == '1' else '1'
    "Simulation"
    # def findKthBit(self, n: int, k: int) -> str:
    #     s = "0"
    #     def invert(ss):
    #         ss = ''.join('1' if x == '0' else '0' for x in ss)
    #         return ss
    #     for i in range(n):
    #         s = s + "1" + invert(s)[::-1]
    #     return s[k-1]