'''
Given an integer n, return the number of prime numbers that are strictly less than n.
Input: n = 10
Output: 4
Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.
'''

# using Sieve of Eratosthenes
class Solution:
    def countPrimes(self, n: int) -> int:
        arr = [True] * n
        if n == 0 or n == 1:
            return 0

        arr[0], arr[1] = False, False

        for i in range(2, int(n ** 0.5) + 1):
            if arr[i]:
                for j in range(i ** 2, n, i):
                    arr[j] = False

        return sum(arr)
