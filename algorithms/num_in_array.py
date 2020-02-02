"""
given an array of integers. Consider the whole array as a single integer.
Increase the single integer by 1 and return as an array
For example:
Input: [1,2,3]
Output: [1,2,4]
"""

def increase_arr(arr):
    carry = 1
    ret = [None] *len(arr)
    for i, val in reversed(list(enumerate(arr))):
        s = val + carry
        ret[i] = s%10
        carry = 0 if s < 10 else 1
    if carry == 1:
        ret =[1] + [0]*len(arr)
    return ret

print(increase_arr([1,2,3]))
print(increase_arr([1,2,9]))
print(increase_arr([9,9,9]))
