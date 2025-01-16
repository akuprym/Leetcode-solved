'''''''''
9.Palindrome Number
Given an integer x, return true if x is a palindrome, and false otherwise.
Example 1:
Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.
'''''''''

# With converting int to str
class Solution:
    def isPalindrome(self, x: int) -> bool:
        x = str(x)
        rev_x = x[::-1]
        return rev_x == x

# W/out converting to str
class Solution:
    def isPalindrome(self, x: int) -> bool:
        def reverse(x):
            r = 0
            while x > 0:
                r *= 10
                r += x % 10
                x //= 10
            return r

        return x == reverse(x)
