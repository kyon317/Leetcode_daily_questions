"""
Leetcode 1813. Sentence Similarity III
https://leetcode.com/problems/sentence-similarity-iii/description/
Finish date: 2024-10-04
Algorithm: Two pointers
"""
class Solution:
    def areSentencesSimilar(self, st1: str, st2: str) -> bool:
        s1, s2 = st1.split(" "), st2.split(" ")
        n, m = len(s1), len(s2)
        if n > m:
            return self.areSentencesSimilar(st2, st1)
        # l: consecutive # of match from left, r: consecutive # of match from right
        l, r = 0, 0

        while l < n and s1[l] == s2[l]:
            l += 1

        while r < n - l and s1[n - r - 1] == s2[m - r - 1]:
            r += 1

        return l + r == n
