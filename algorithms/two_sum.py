"""
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
"""
   
class Solution:
    def twoSum(self, nums: [int], target: int) -> [int]:
        h = {}
        for i, val in enumerate(nums):                    
            remain = target - val            
            j = h.get(remain)            
            if j is not None and i != j:
                return i, j
            h[val] = i
    # when the array is sorted
    def twoSum_2pointer(self, numbers, target):
        l, r = 0, len(numbers)-1
        while l < r:
            s = numbers[l] + numbers[r]
            if s == target:
                return [l+1, r+1]
            elif s < target:
                l += 1
            else:
                r -= 1
    def twoSum_binarySearch(self, numbers, target):
        for i in xrange(len(numbers)):
            l, r = i+1, len(numbers)-1
            tmp = target - numbers[i]
            while l <= r:
                mid = l + (r-l)//2
                if numbers[mid] == tmp:
                    return [i+1, mid+1]
                elif numbers[mid] < tmp:
                    l = mid+1
                else:
                    r = mid-1

                
                
s = Solution()
print(s.twoSum([3,2,4], 6))