''''''''''
136. Single Number
Given a no n-empty array of integers nums, every element appears twice except for one. Find that single one.

You must implement a solution with a linear runtime complexity and use only constant extra space.

Example 1:
Input: nums = [2 ,2 ,1]
Output: 1
''''''''''

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        result = 0
        for i in nums:
            result ^= i  # XOR all elements
        return result

# XORing all elements cancels out duplicates (a ^ a = 0) and leaves the unique number.