from typing import List

'''
Leetcode 1590. Make Sum Divisible by P
https://leetcode.com/problems/make-sum-divisible-by-p/description/
Finish date: 2024-10-02
Algorithm: Math
'''

class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        x = sum(nums) % p
        if x == 0: return 0

        res = n = len(nums)
        s = 0
        last = {s: -1}
        for i, v in enumerate(nums):
            s += v
            last[s % p] = i
            j = last.get((s - x) % p, -n)  # -n to guarantee i-j >= n
            if res > i - j:
                res = i - j
        return res if res < n else -1