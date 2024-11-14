"""
Leetcode 2064. Minimized Maximum of Products Distributed to Any Store
https://leetcode.com/problems/minimized-maximum-of-products-distributed-to-any-store/description/
Finish date: 2024-11-13
Algorithm: Binary Search
"""
import math
from typing import List


class Solution:
    def minimizedMaximum(self, n: int, quantities: List[int]) -> int:
        tt = sum(quantities)
        l,r = 1,max(quantities)
        def check(x):
            res = sum(math.ceil(q / x) for q in quantities)
            return res <= n
        while l < r:
            mid = (l + r) // 2
            if check(mid):
                r = mid
            else:
                l = mid + 1
        return l