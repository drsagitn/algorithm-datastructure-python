"""
Given two strings s and t , write a function to determine if t is an anagram of s.

Example 1:

Input: s = "anagram", t = "nagaram"
Output: true
Example 2:

Input: s = "rat", t = "car"
Output: false
Note:
You may assume the string contains only lowercase alphabets.

Follow up:
What if the inputs contain unicode characters? How would you adapt your solution to such case?
"""
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        m1 = m2 = 1
        s1 = s2 = 0
        for c in s:
            m1 *= ord(c)
            s1 += ord(c)
        for c in t:
            m2 *= ord(c)
            s2 += ord(c)
        if str(m1)+str(s1) == str(m2)+str(s2):
            return True
        return False
    
    def isAnagram2(self, s: str, t: str) -> bool:
        hashmap = {}
        for c in s:
            if hashmap.get(c) is None:
                hashmap[c] = 1
            else:
                hashmap[c] += 1
        for c in t:
            if hashmap.get(c) is None or hashmap.get(c) <= 0:
                return False
            else:
                hashmap[c] -= 1
        return True

s =Solution()
print(s.isAnagram2("anagram","nagaram"))