# The Hamming distance between two integers is the number of positions at which the corresponding bits are different.

# Given two integers x and y, calculate the Hamming distance.

# Note:
# 0 ≤ x, y < 231.

# Example:

# Input: x = 1, y = 4

# Output: 2

# Explanation:
# 1   (0 0 0 1)
# 4   (0 1 0 0)
#        ↑   ↑

# The above arrows point to positions where the corresponding bits are different.
class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        a = [int(t) for t in bin(x)[2:]]
        b = [int(k) for k in bin(y)[2:]]
        n = len(a) - len(b)
        padding_arr = [0 for i in range(abs(n))]
        if(n>0):
            b = padding_arr + b
        else:
            a = padding_arr + a
        ret = 0
        for i in range(len(a)):
            if(a[i]+b[i] == 1):
                ret+=1
        return ret
            
a = Solution()
print(a.hammingDistance(1, 4))