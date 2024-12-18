"""
Leetcode 1475. Final Prices With a Special Discount in a Shop
https://leetcode.com/problems/final-prices-with-a-special-discount-in-a-shop/description/
Finish date: 2024-12-17
Algorithm: Monotonic Stack
"""
from typing import List


class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        n = len(prices)
        res = [-1] * n
        stk = []

        for i in range(n - 1, -1, -1):
            while stk and stk[-1] > prices[i]:
                stk.pop()
            res[i] = stk[-1] if stk else -1
            stk.append(prices[i])
        for i in range(n):
            res[i] = prices[i] - res[i] if res[i] != -1 else prices[i]
        return res
