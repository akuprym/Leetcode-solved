''''''''''
Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.
Assume the environment does not allow you to store 64-bit integers (signed or unsigned).
Input: x = 123
Output: 321
'''''''''''

class Solution:
    def reverse(self, x: int) -> int:
        INT_MIN, INT_MAX = -2**31, 2**31 - 1  # Define 32-bit limits
        sign = -1 if x < 0 else 1
        x = abs(x)
        reversed_x = 0

        while x != 0:
            digit = x % 10
            x //= 10
            if ( reversed_x > INT_MAX // 10) or ( reversed_x == INT_MAX // 10 and digit > 7):
                return 0  # Overflow case
            if ( reversed_x < INT_MIN // 10) or ( reversed_x == INT_MIN // 10 and digit > 8):
                return 0  # Underflow case
            reversed_x = reversed_x * 10 + digit

        return reversed_x * sign
