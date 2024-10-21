"""
Leetcode 1593. Split a String Into the Max Number of Unique Substrings
https://leetcode.com/problems/split-a-string-into-the-max-number-of-unique-substrings/
Finish date: 2024-10-21
Algorithm: Backtracking
"""

class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        st = set()
        n = len(s)
        res = 0

        def dfs(i, curr):
            nonlocal res
            if i == len(curr):
                res = max(len(st), res)
                return
            dfs(i + 1, curr)
            sub_s = curr[: i + 1]
            if sub_s not in st:
                st.add(sub_s)
                dfs(0, curr[i + 1 :])
                st.remove(sub_s)

        dfs(0, s)
        return res
