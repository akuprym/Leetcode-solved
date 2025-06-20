"""
You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing the number of elements in nums1 and nums2 respectively.
Merge nums1 and nums2 into a single array sorted in non-decreasing order.
The final sorted array should not be returned by the function, but instead be stored inside the array nums1. To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, and the last n elements are set to 0 and should be ignored. nums2 has a length of n.
Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
Output: [1,2,2,3,5,6]
"""

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        k = m + n -1 # Last index of nums1
        while m > 0 and n > 0:
            if nums1[m-1] > nums2[n-1]: # Pick larger element
                nums1[k] = nums1[m-1]
                m -= 1
            else:
                nums1[k] = nums2[n-1]
                n -= 1
            k -= 1  # Move the pointer for nums1

        # If any elements remain in nums2
        if n > 0:
            nums1[:n] = nums2[:n]


#straightforward approach
def merge(self, nums1, m, nums2, n):
nums1[m:] = nums2[:n]
nums1.sort()


"""
Key ideas:
- Start filling from the end of nums1
- Compare elements from both arrays and put larger one at the end
"""
