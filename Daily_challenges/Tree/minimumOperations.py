"""
Leetcode 2471. Minimum Number of Operations to Sort a Binary Tree by Level
https://leetcode.com/problems/minimum-number-of-operations-to-sort-a-binary-tree-by-level/description/
Finish date: 2024-12-22
Algorithm: BFS, Cycle
"""
from collections import deque
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def minimumOperations(self, root: Optional[TreeNode]) -> int:
        q = deque([root])
        ans = 0
        while q:
            sz = len(q)
            tmp = []

            for _ in range(sz):
                curr = q.popleft()
                tmp.append(curr.val)
                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)
            n = len(tmp)
            a = sorted(range(n), key=lambda i: tmp[i])

            ans += n
            vis = [False] * n
            for v in a:
                if vis[v]: continue
                while not vis[v]:
                    vis[v] = True
                    v = a[v]
                ans -= 1
        return ans