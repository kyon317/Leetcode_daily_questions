"""
Leetcode 2235. Add Two Integers
https://leetcode.com/problems/add-two-integers/
Finish date: 2024-10-21
Algorithm: Bit Operation
"""

class Solution:
    def sum(self, num1: int, num2: int) -> int:
        MAX_INT = 0x7FFFFFFF
        MIN_INT = 0x80000000
        MASK = 0xFFFFFFFF
        print(num1 << num2)
        while num2 != 0:
            curr_sum = (num1 ^ num2) & MASK
            carry = ((num1 & num2) << 1) & MASK

            num1 = curr_sum
            num2 = carry
        return num1 if num1 <= MAX_INT else ~(num1 ^ MASK)