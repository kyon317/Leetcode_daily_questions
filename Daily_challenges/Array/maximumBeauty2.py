"""
Leetcode 2779. Maximum Beauty of an Array After Applying Operation
https://leetcode.com/problems/maximum-beauty-of-an-array-after-applying-operation/description/
Finish date: 2024-12-10
Algorithm: Two pointers
"""

from typing import List


class Solution:
    def maximumBeauty(self, nums: List[int], k: int) -> int:
        res, l = 0, 0
        nums.sort()
        for r in range(len(nums)):
            while nums[r] - nums[l] > 2 * k:
                l += 1
            res = max(res, r - l + 1)
        return res