
"""
LeetCode: Palindrome Number
URL: https://leetcode.com/problems/palindrome-number/
Difficulty: Easy
"""

class Solution:
    def isPalindrome(self, x: int) -> bool:
        return str(x)[::-1] == str(x)


