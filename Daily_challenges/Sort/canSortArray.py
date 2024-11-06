"""
Leetcode 3011. Find if Array Can Be Sorted
https://leetcode.com/problems/find-if-array-can-be-sorted/description/
Finish date: 2024-11-05
Algorithm: Sort
"""
class Solution:
    def canSortArray(self, nums: List[int]) -> bool:
        bn = [x.bit_count() for x in nums]
        idx = 0
        segs = []
        bb = bn[0]
        for i,(x,b) in enumerate(zip(nums,bn)):
            if b != bb:
                segs.append(nums[idx:i])
                idx = i
                bb = b
        segs.append(nums[idx:])
        segs = [sorted(x) for x in segs]
        prev = segs[0][-1]
        for seg in segs[1:]:
            if seg[0] < prev:
                return False
            prev = seg[-1]
        return True