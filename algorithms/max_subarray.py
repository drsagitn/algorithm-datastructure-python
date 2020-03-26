"""
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

Example:

Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
"""
import collections
class Solution:
    def maxSubArray(self, nums: [int]) -> int:
        max_sum = cur_sum = float('-inf')
        for num in nums:
            cur_sum = max(num+cur_sum, num)
            max_sum = max(cur_sum, max_sum)
        return max_sum

    def maxSlidingWindow2(self, nums, k):
        d = collections.deque()
        out = []
        for i, n in enumerate(nums):
            while d and nums[d[-1]] < n:
                d.pop()
            d += i,
            if d[0] == i - k:
                d.popleft()
            if i >= k - 1:
                out += nums[d[0]],
        return out

s = Solution()
print(s.maxSlidingWindow2([1,3,-1,-3,5,3,6,7], 3))