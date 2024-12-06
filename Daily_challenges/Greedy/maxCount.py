"""
Leetcode 2554. Maximum Number of Integers to Choose From a Range I
https://leetcode.com/problems/maximum-number-of-integers-to-choose-from-a-range-i/description/
Finish date: 2024-12-05
Algorithm: Greedy
"""
from typing import List

class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        sm = 0
        cnt = 0
        ban = set(banned)
        for i in range(1,n+1):
            if i not in ban:
                sm += i
                if sm > maxSum:
                    return cnt
                cnt += 1
        return cnt