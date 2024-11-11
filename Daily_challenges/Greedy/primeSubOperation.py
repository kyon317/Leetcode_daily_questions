"""
Leetcode 2601. Prime Subtraction Operation
https://leetcode.com/problems/prime-subtraction-operation/
Finish date: 2024-11-10
Algorithm: Greedy, Binary Search
"""
from bisect import bisect_left
from typing import List

p = [0]
is_prime = [True] * 1000
# prime sieve
for i in range(2,1000):
    if is_prime[i]:
        p.append(i)
    for j in range(i*i,1000,i):
        is_prime[j] = False
class Solution:
    def primeSubOperation(self, nums: List[int]) -> bool:
        pre = 0
        for x in nums:
            if x <= pre:
                return False
            mx_p = p[bisect_left(p,x - pre) - 1] # find max p that pre < x-p
            pre = x - mx_p
        return True