"""
Leetcode 2461. Maximum Sum of Distinct Subarrays With Length K
https://leetcode.com/problems/maximum-sum-of-distinct-subarrays-with-length-k/description/
Finish date: 2024-11-18
Algorithm: Sliding Window, Hashmap
"""

from collections import Counter
from typing import List


class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        res = 0
        n = len(nums)
        start,end = 0,k-1
        cnt = Counter(nums[:k])
        window_sum = sum(nums[:k])
        if len(cnt) == k:
                res = max(res, window_sum)
        while end < n - 1:
            cnt[nums[start]] -= 1
            cnt[nums[end + 1]] += 1
            window_sum -= nums[start]
            window_sum += nums[end + 1]
            if cnt[nums[start]] == 0:
                del cnt[nums[start]]
            if len(cnt) == k:
                res = max(res, window_sum)
            start += 1
            end += 1

        return res