"""
Leetcode 515. Find Largest Value in Each Tree Row
https://leetcode.com/problems/find-largest-value-in-each-tree-row/description/
Finish date: 2024-12-24
Algorithm: BFS
"""
from collections import deque
from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        q = deque([root])
        if not root:
            return res
        while q:
            sz = len(q)
            temp = []
            for _ in range(sz):
                curr = q.popleft()
                temp.append(curr.val)
                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)
            res.append(max(temp))
        return res