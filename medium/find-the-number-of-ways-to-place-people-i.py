"""
LeetCode: Find the Number of Ways to Place People I
URL: https://leetcode.com/problems/find-the-number-of-ways-to-place-people-i
Difficulty: Medium
"""

class Solution:
    def numberOfPairs(self, points: List[List[int]]) -> int:
        res = 0
        n = len(points)

        for i in range(n):
            x1, y1 = points[i]
            for j in range(n):
                if i == j:
                    continue
                x2, y2 = points[j]
                        
                if x1 > x2 or y1 < y2:
                    continue

                flag = True
                for k in range(n):
                    if k == i or k == j:
                        continue
                    x, y = points[k]
                    if x >= x1 and x <= x2 and y <= y1 and y >= y2:
                        flag = False
                        break

                if flag:
                    res += 1
        return res


