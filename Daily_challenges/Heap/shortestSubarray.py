"""
Leetcode 862. Shortest Subarray with Sum at Least K
https://leetcode.com/problems/shortest-subarray-with-sum-at-least-k/description/
Finish date: 2024-11-17
Algorithm: Monotonic Stack, Presum
"""
from collections import deque
from itertools import accumulate
from math import inf
from typing import List


class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        n = len(nums)
        presum = list(accumulate(nums, initial=0)) # presum
        q = deque() # monotonic stack q
        res = inf
        for i, x in enumerate(presum):
            # for left,right in presum, if presum[left] - presum[right] >= k, leftend should be removed
            while q and x - presum[q[0]] >= k:
                res = min(res, i - q.popleft())
            # for left,right in presum, presum[right] <= presum[left] , rightend should be removed
            while q and x <= presum[q[-1]]:
                q.pop()
            q.append(i)
        return res if res < inf else -1