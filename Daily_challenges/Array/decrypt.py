"""
Leetcode 1652. Defuse the Bomb
https://leetcode.com/problems/defuse-the-bomb/description/
Finish date: 2024-11-17
Algorithm: Simulation, Sliding Window
"""

from typing import List


class Solution:
    # Sliding Window
    def decrypt(self, code: List[int], k: int) -> List[int]:
        n = len(code)
        res = [0] * n
        if k == 0:
            return res

        start, end = (1, k + 1) if k > 0 else (k, 0)
        window_sum = sum(code[i % n] for i in range(start, end))

        for i in range(n):
            res[i] = window_sum
            window_sum -= code[(i + start) % n] # pop left
            window_sum += code[(i + end) % n] # add right
        return res
    # Brute Force
    # def decrypt(self, code: List[int], k: int) -> List[int]:
    #     n = len(code)
    #     res = [0] * n
    #     if k == 0:
    #         return res
    #     s = abs(k)
    #     for i, x in enumerate(code):
    #         curr = 0
    #         for j in range(s):
    #             if k > 0:
    #                 idx = (i + j + 1) % n
    #             else:
    #                 idx = (i - j - 1) % n
    #             curr += code[idx]
    #         res[i] = curr
    #     return res