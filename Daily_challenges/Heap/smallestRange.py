"""
Leetcode 632. Smallest Range Covering Elements from K Lists
https://leetcode.com/problems/smallest-range-covering-elements-from-k-lists/description/
Finish date: 2024-10-12
Algorithm: Greedy, MinHeap
"""
import heapq
from typing import List


class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        rangeLeft, rangeRight = -10 ** 9, 10 ** 9
        maxValue = max(vec[0] for vec in nums)
        priorityQueue = [(vec[0], i, 0) for i, vec in enumerate(nums)]
        heapq.heapify(priorityQueue)

        while True:
            minValue, row, idx = heapq.heappop(priorityQueue)
            if maxValue - minValue < rangeRight - rangeLeft:
                rangeLeft, rangeRight = minValue, maxValue
            if idx == len(nums[row]) - 1:
                break
            maxValue = max(maxValue, nums[row][idx + 1])
            heapq.heappush(priorityQueue, (nums[row][idx + 1], row, idx + 1))

        return [rangeLeft, rangeRight]