"""
Leetcode 2762. Continuous Subarrays
https://leetcode.com/problems/continuous-subarrays/description/
Finish date: 2024-12-13
Algorithm: Array, Sliding window
"""
from collections import Counter
from typing import List


class Solution:
    def continuousSubarrays(self, nums: List[int]) -> int:
        res = l = 0
        cnt = Counter()
        for r, x in enumerate(nums):
            cnt[x] += 1
            while max(cnt) - min(cnt) > 2:
                curr = nums[l]
                cnt[curr] -= 1
                if cnt[curr] == 0:
                    del cnt[curr]
                l += 1
            res += r - l + 1
        return res