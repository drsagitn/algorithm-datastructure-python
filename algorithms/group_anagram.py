"""
Given an array of strings, group anagrams together.

Example:

Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
Output:
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]
Note:

All inputs will be in lowercase.
The order of your output does not matter.
"""
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = {}
        for s in strs:
            mul = 1
            summation = 0
            for c in s:
                mul *= ord(c)
                summation += ord(c)
            _id = str(mul)+str(summation)
            if not hashmap.get(_id):
                hashmap[_id] = []    
            hashmap[_id].append(s)
        return hashmap.values()
                
class Solution2:
    def groupAnagrams(strs):
        ans = collections.defaultdict(list)
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            ans[tuple(count)].append(s)
        return ans.values()