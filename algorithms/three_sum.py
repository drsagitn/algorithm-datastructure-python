"""
Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Note:

The solution set must not contain duplicate triplets.

Example:

Given array nums = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]
"""
class Solution:        
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ret = []
        nums.sort()
        length = len(nums)
        for i, num in enumerate(nums):
            if i>0 and num == nums[i - 1]:
                continue
            target = num*-1            
            l = i + 1
            r = length -1
            
            while l < r:
                if nums[l] + nums[r] > target:
                    r -= 1
                elif nums[l] + nums[r] < target:
                    l += 1
                else:
                    ret.append([num, nums[l], nums[r]])
                    l += 1
                    r -= 1
            
                    while l < r and nums[l] == nums[l-1]:
                        l += 1
                    while l < r and r < length-1 and nums[r] == nums[r+1]:
                        r -= 1
                    
                
        return ret
                