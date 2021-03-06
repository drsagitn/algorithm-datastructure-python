"""
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it is able to trap after raining.
Input: [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
"""

class Solution:
    def trap(self, height: List[int]) -> int:
        left = 0
        right = len(height)-1
        left_max = 0
        right_max = 0
        ret = 0
        while left < right:
            if height[left] < height[right]:
                if height[left] >= left_max:
                    left_max = height[left]
                else:
                    ret += left_max - height[left]
                left += 1
            else:
                if height[right] >= right_max:
                    right_max = height[right]
                else:
                    ret += right_max - height[right]
                right -= 1
        return ret