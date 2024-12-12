"""
Leetcode 2558. Take Gifts From the Richest Pile
https://leetcode.com/problems/take-gifts-from-the-richest-pile/description/
Finish date: 2024-12-11
Algorithm: Heap
"""

from heapq import heapify, heapreplace
from math import isqrt
from typing import List


class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        for i in range(len(gifts)):
            gifts[i] *= -1
        heapify(gifts)
        while k and -gifts[0] > 1:
            heapreplace(gifts, -isqrt(-gifts[0]))
            k -= 1
        return -sum(gifts)