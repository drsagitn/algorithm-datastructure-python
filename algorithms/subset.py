class Solution:
    def subsets(self, nums: [int]) -> [[int]]:
        def backtrack(first = 0, curr = []):            
            # if the combination is done
            if len(curr) == k:  
                output.append(curr[:])
            for i in range(first, n):
                # add nums[i] into the current combination
                curr.append(nums[i])
                # use next integers to complete the combination
                backtrack(i + 1, curr)
                # backtrack
                curr.pop()
        
        output = []
        n = len(nums)
        for k in range(n + 1):
            backtrack()
        return output

a = Solution()
print(a.subsets([1,2,3,4,5]))