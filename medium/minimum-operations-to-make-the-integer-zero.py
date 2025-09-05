"""
LeetCode: Minimum Operations to Make the Integer Zero
URL: https://leetcode.com/problems/minimum-operations-to-make-the-integer-zero/
Difficulty: Medium
"""

class Solution:
    def makeTheIntegerZero(self, num1: int, num2: int) -> int:
        max_k = num1 // (num2 + 1) if num2 > 0 else 1000

        for k in range(1, max_k + 1):
            S = num1 - k * num2
            if S < k:
                continue
            if bin(S).count('1') <= k:
                return k

        return -1


