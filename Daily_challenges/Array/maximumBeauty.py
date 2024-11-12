"""
Leetcode 2070. Most Beautiful Item for Each Query
https://leetcode.com/problems/most-beautiful-item-for-each-query/description/
Finish date: 2024-11-11
Algorithm: Array, Sort
"""
from typing import List


class Solution:
    def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:
        items = sorted(items, key = lambda x: x[0])
        n = len(queries)
        res = [0] * n
        qlist = sorted(zip(queries,range(n)))
        j = 0
        mx = 0
        for q, idx in qlist:
            while j < len(items) and items[j][0] <= q:
                mx = max(items[j][1], mx)
                j += 1
            res[idx] = mx
        return res