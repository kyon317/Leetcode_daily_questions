"""
Leetcode 1963. Minimum Number of Swaps to Make the String Balanced
https://leetcode.com/problems/minimum-number-of-swaps-to-make-the-string-balanced/description/
Finish date: 2024-10-07
Algorithm: Greedy
"""

class Solution:
    def minSwaps(self, s: str) -> int:
        cnt, res = 0, 0
        for x in s:
            # increment if [
            if x == "[":
                cnt += 1
            # decrement if ] and cnt > 0
            elif cnt > 0:
                cnt -= 1
            # swap
            else:
                cnt += 1
                res += 1
        return res
