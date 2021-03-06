"""
Count the number of prime numbers less than a non-negative number, n.

Example:

Input: 10
Output: 4
Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.
Sieve of Eratosthenes
"""
class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 1:
            return 0
        arr = [1]*n
        arr[0] = 0
        arr[1] = 0
        for i in range(2,int(n/2)+1):
            if arr[i] is not 0:
                arr[i*i:n:i] = [0] * len(arr[i*i:n:i])                
        return sum(arr)