"""
Leetcode 1792. Maximum Average Pass Ratio
https://leetcode.com/problems/maximum-average-pass-ratio/description/
Finish date: 2024-12-14
Algorithm: Greedy, Heap
"""
from heapq import heappush, heappop
from typing import List


class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        def get_gain(p, t):
            return (p + 1) / (t + 1) - p / t
        heap = []
        for p, t in classes:
            heappush(heap, (-get_gain(p, t), p, t))
        for _ in range(extraStudents):
            g, p, t = heappop(heap)
            p += 1
            t += 1
            g = get_gain(p, t)
            heappush(heap, (-g, p, t))
        res = 0.0
        for _, p, t in heap:
            res += p / t
        return res / len(classes)
