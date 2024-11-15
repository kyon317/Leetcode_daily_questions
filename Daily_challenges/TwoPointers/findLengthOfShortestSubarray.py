"""
Leetcode 1574. Shortest Subarray to be Removed to Make Array Sorted
https://leetcode.com/problems/shortest-subarray-to-be-removed-to-make-array-sorted/description/
Finish date: 2024-11-14
Algorithm: Two Pointers
"""
from typing import List


class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        n = len(arr)
        right = n - 1
        while right and arr[right - 1] <= arr[right]:
            right -= 1
        if right == 0:
            return 0
        res = right  # start from delete all on the left
        left = 0
        while left == 0 or arr[left - 1] <= arr[left]:
            while right < n and arr[left] > arr[right]:
                right += 1
            left += 1
            res = min(res, right - left)  # delete (left, right)
        return res
