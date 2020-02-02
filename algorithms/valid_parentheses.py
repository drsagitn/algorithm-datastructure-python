"""
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Note that an empty string is also considered valid.

Example 1:

Input: "()"
Output: true
Example 2:

Input: "()[]{}"
Output: true
Example 3:

Input: "(]"
Output: false
Example 4:

Input: "([)]"
Output: false
Example 5:

Input: "{[]}"
Output: true
"""
class Solution:
    def isValid(self, s: str) -> bool:        
        stack = []
        openings = ["(", "{", "["]        
        bracket_map = {"(": ")", "[": "]",  "{": "}"}
        
        for c in s:
            if c in openings:
                stack.append(c)
            elif len(stack) == 0 or c != bracket_map.get(stack.pop()):
                return False
        if len(stack) > 0:
            return False
        return True
                
    