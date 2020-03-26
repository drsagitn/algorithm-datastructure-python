"""
Given an array nums of n integers where n > 1,  return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].

Example:

Input:  [1,2,3,4]
Output: [24,12,8,6]
Constraint: It's guaranteed that the product of the elements of any prefix or suffix of the array (including the whole array) fits in a 32 bit integer.

Note: Please solve it without division and in O(n).

Follow up:
Could you solve it with constant space complexity? (The output array does not count as extra space for the purpose of space complexity analysis.)
"""
class Solution:
    def productExceptSelf(self, nums: [int]) -> [int]:
        ret = [1]*len(nums)        
        i = 1
        while i < len(nums):
            ret[i] = ret[i-1]*nums[i-1]
            i += 1
        r = 1
        i = len(nums)-1
        while i >= 0:
            ret[i] = ret[i]*r
            r = r * nums[i]
            i -= 1
        return ret
            
s = Solution()
print(s.productExceptSelf([1,2,3,4]))