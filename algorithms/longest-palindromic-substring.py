"""
Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

Example 1:

Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.
Example 2:

Input: "cbbd"
Output: "bb"
"""
class Solution:
    def longestPalindrome(self, s: str) -> str:
        max_string = ""
        for i in range(len(s)):
            l1, s1 = self.expandFromCenter(i, i, s)
            l2, s2 = self.expandFromCenter(i, i+1, s)
            if l1 > l2:
                target_str = s1
            else:
                target_str = s2
            if len(max_string) < len(target_str):
                max_string = target_str
        return max_string
            
            
    def expandFromCenter(self, left, right, s):        
        while left >=0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return right-left-1, s[left+1:right]
        
s = Solution()
print(s.longestPalindrome("aaaaaa"))