"""
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent.

A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.

Example:

Input: "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
Note:

Although the above answer is in lexicographical order, your answer could be in any order you want.

Accepted
"""
class Solution:
    def letterCombinations(self, digits: str):
        phone = {'2': ['a', 'b', 'c'],
                 '3': ['d', 'e', 'f'],
                 '4': ['g', 'h', 'i'],
                 '5': ['j', 'k', 'l'],
                 '6': ['m', 'n', 'o'],
                 '7': ['p', 'q', 'r', 's'],
                 '8': ['t', 'u', 'v'],
                 '9': ['w', 'x', 'y', 'z']}
        if not digits or len(digits) == 0:
            return []
       
        def recursive_get(left_digits, current_str):
            if len(left_digits) == 0:
                ret.append(current_str)
            else:
                for letter in phone[left_digits[0]]:
                    recursive_get(left_digits[1:], current_str+letter)
    
        ret = []
        str_ =  ""
        recursive_get(digits, str_)
        return ret
        