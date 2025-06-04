'''
You are climbing a staircase. It takes n steps to reach the top.
Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step
'''

# Hint: For n >= 3, the number of ways to reach step n is the sum of the ways to reach steps n-1 and n-2.

class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 3: return n
        first = 1
        second = 2
        for i in range(3, n+1):
            third = first + second
            first = second
            second = third
        return second