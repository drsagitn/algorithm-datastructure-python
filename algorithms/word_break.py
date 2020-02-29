"""
Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, determine if s can be segmented into a space-separated sequence of one or more dictionary words.

Note:

The same word in the dictionary may be reused multiple times in the segmentation.
You may assume the dictionary does not contain duplicate words.
Example 1:

Input: s = "leetcode", wordDict = ["leet", "code"]
Output: true
Explanation: Return true because "leetcode" can be segmented as "leet code".
Example 2:

Input: s = "applepenapple", wordDict = ["apple", "pen"]
Output: true
Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
             Note that you are allowed to reuse a dictionary word.
Example 3:

Input: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
Output: false
"""
class Solution:    
        
    def wordBreak(self, s: str, wordDict: [str]) -> bool:
        graph = {}
        def helper(word):
            if graph.get(word) is not None:
                return graph[word]
            for w in wordDict:                
                if word[:len(w)] == w:
                    if word[len(w):] == "":
                        graph[word] = True
                        return True
                    if helper(word[len(w):]) == True:
                        return True
            graph[word] = False
            return False
        return helper(s)

s = Solution()
print(s.wordBreak("catsandog", ["cats", "dog", "sand", "and", "cat"]))