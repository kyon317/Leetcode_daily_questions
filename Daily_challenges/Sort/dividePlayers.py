'''
Leetcode 2491. Divide Players Into Teams of Equal Skill
https://leetcode.com/problems/divide-players-into-teams-of-equal-skill/description/
Finish date: 2024-10-03
Algorithm: Sorting, Hashtable
'''
from typing import List


class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        ans, target = 0, skill[0] + skill[-1]
        for i in range(len(skill) // 2):
            x, y = skill[i], skill[-1 - i]
            if x + y != target: return -1
            ans += x * y
        return ans