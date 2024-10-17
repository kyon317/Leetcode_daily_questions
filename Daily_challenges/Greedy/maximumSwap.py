"""
Leetcode 670. Maximum Swap
https://leetcode.com/problems/maximum-swap/description/
Finish date: 2024-10-16
Algorithm: Greedy
"""

class Solution:
    def maximumSwap(self, num: int) -> int:
        arr = list(str(num))
        n = len(arr)
        mx_i = n - 1
        l,r = -1,-1
        for i in range(n - 2,-1,-1):
            if arr[i] > arr[mx_i]:
                mx_i = i
            elif arr[i] < arr[mx_i]:
                l,r = i, mx_i
        if l == -1:
            return num
        arr[l],arr[r] = arr[r],arr[l]
        return int(''.join(arr))