'''''''''
1748. Sum of Unique Elements
You are given an integer array nums. The unique elements of an array are the elements that appear exactly once in the array.
Return the sum of all the unique elements of nums.
Example 1:
Input: nums = [1,2,3,2]
Output: 4
Explanation: The unique elements are [1,3], and the sum is 4.
'''''''''

class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        n = []
        u = []
        for i in nums:
            if i not in n:
                n.append(i)
                u.append(i)
            elif i in u:
                u.remove(i)
        return sum(u)


# 2.Using a dict to count the frequency of each number.
class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        d = {}
        for i in nums:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1
        sum = 0
        for i, v in d.items():
            if v == 1:
                sum += i
        return sum
