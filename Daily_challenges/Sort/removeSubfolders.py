"""
Leetcode 1233. Remove Sub-Folders from the Filesystem
https://leetcode.com/problems/remove-sub-folders-from-the-filesystem/description/
Finish date: 2024-10-24
Algorithm: Sorting
"""

from typing import List


class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        folder.sort()
        res = []
        res.append(folder[0])
        for x in folder[1:]:
            m,n = len(res[-1]), len(x)
            if m >= n:
                res.append(x)
            elif not (x[:m] == res[-1] and x[m] == '/'):
                res.append(x)
        return res