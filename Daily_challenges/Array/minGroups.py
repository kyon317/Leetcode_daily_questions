"""
Leetcode 2406. Divide Intervals Into Minimum Number of Groups
https://leetcode.com/problems/divide-intervals-into-minimum-number-of-groups/description/
Finish date: 2024-10-11
Algorithm: Heap, Difference
"""

from heapq import heappush, heapreplace
from typing import List


class Solution:
    """MinHeap"""
    def minGroups(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x: x[0])
        h = []
        for start, end in intervals:
            # overlap, create new heap
            if h and h[0] < start:
                heapreplace(h, end)
            # start > current end, append to end
            else:
                heappush(h, end)
        return len(h)

    # """Difference"""
    # def minGroups(self, intervals: List[List[int]]) -> int:
    #     diff = [0] * (1000010)
    #     res, curr = diff[0], diff[0]
    #     for start, end in intervals:
    #         diff[start] += 1
    #         diff[end + 1] -= 1
    #     for x in diff:
    #         curr += x
    #         if curr > res:
    #             res = curr
    #     return res

    # """Brute Force (TLE)"""
    # def minGroups(self, intervals: List[List[int]]) -> int:
    #     intervals.sort(key = lambda x: x[1])
    #     mx = intervals[-1][1]

    #     time = [0] * (mx + 1)
    #     for start, end in intervals:
    #         for i in range(start, end + 1):
    #             time[i] += 1

    #     return max(time)
