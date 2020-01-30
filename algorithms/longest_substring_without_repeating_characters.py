"""
Given a string, find the length of the longest substring without repeating characters.

Example 1:

Input: "abcabcbb"
Output: 3 
Explanation: The answer is "abc", with the length of 3. 
Example 2:

Input: "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3. 
             Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
"""
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        hash_map = {}
        i = j = ans = 0
        while j < len(s):
            sIdx = hash_map.get(s[j])
            hash_map[s[j]] = j
            if sIdx is not None:            
                ans = max(j-i, ans)                
                if i <= sIdx:
                    i = sIdx + 1
            j += 1
        return max(ans, j-i)
0 1 2 3
c b b d

i = 1
l = 2
abs(int(i - round((max_len-1)/2)))
(2-1)/2 = 0 => start = abs(1-0) = 1
(3-1)/2 = 1 => start = abs(1-1) = 0
(4-1)/2 = 1
(5-1)/2 = 2
(6-1)/2 = 2