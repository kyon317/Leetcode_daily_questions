"""
Leetcode 3133. Minimum Array End
https://leetcode.com/problems/minimum-array-end/description/
Finish date: 2024-11-08
Algorithm: Bit Operation
"""
class Solution:
    def minEnd(self, n: int, x: int) -> int:
        res = []
        curr = bin(x)[-1:1:-1]
        fill = bin(n-1)[-1:1:-1]
        idx = 0
        for i, bit in enumerate(curr):
            if bit == '1':
                res.append(bit)
            else:
                res.append(fill[idx])
                idx += 1
                if idx == len(fill):
                    res.append(curr[i+1:])
                    break
        res.append(fill[idx:])
        a = ''.join(res)[::-1]
        return int(a,2)