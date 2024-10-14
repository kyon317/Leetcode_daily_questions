"""
Leetcode 2530. Maximal Score After Applying K Operations
https://leetcode.com/problems/maximal-score-after-applying-k-operations/
Finish date: 2024-10-13
Algorithm: MinHeap
"""

from heapq import heapify, heappop, heappush, heapreplace
from math import ceil
from typing import List


class Solution:
    """Heap O(1) Space"""
    def maxKelements(self, nums: List[int], k: int) -> int:
        res = 0
        for i in range(len(nums)):
            nums[i] = -nums[i] # Max Heap
        heapify(nums)
        for i in range(k):
            res -= heapreplace(nums, nums[0] // 3)
        return res
    """Heap"""
    # def maxKelements(self, nums: List[int], k: int) -> int:
    #     res = 0
    #     h = [-x for x in sorted(nums)]
    #     heapify(h)
    #     for i in range(k):
    #         x = -heappop(h)
    #         res += x
    #         x = ceil(x / 3)
    #         heappush(h, -x)
    #     return res
