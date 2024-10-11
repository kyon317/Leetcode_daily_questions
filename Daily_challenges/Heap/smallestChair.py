"""
Leetcode 1942. The Number of the Smallest Unoccupied Chair
https://leetcode.com/problems/the-number-of-the-smallest-unoccupied-chair/description/
Finish date: 2024-10-10
Algorithm: Heap, PriorityQueue
"""

from heapq import heappop, heappush
from typing import List


class Solution:
    def smallestChair(self, times: List[List[int]], targetFriend: int) -> int:
        num_chairs = 0
        used = []
        free = []
        lst = sorted(range(len(times)), key=lambda x: times[x][0])
        for idx in lst:
            start, end = times[idx]
            while used and used[0][0] <= start:
                heappush(free, heappop(used)[1])
            if not free:
                heappush(free, num_chairs)
                num_chairs += 1

            chair = heappop(free)
            if idx == targetFriend:
                return chair

            heappush(used, (end, chair))