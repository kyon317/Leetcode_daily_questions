from typing import List
'''
Leetcode 1497. Check If Array Pairs Are Divisible by k
https://leetcode.com/problems/check-if-array-pairs-are-divisible-by-k/
Finish date: 2024-09-30
Algorithm: Math, Counting
'''


class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        cnt = [0] * k
        for x in arr:
            # compute the remainder
            idx = ((x % k) + k) % k
            cnt[idx] += 1
        for i in range(1, k):
            if cnt[i] != cnt[k - i]:
                return False
        # 0 pairs with itself
        return True if cnt[0] % 2 == 0 else False
