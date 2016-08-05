'''
Given an array nums containing n + 1 integers where each integer is
between 1 and n (inclusive), prove that at least one duplicate number
must exist. Assume that there is only one duplicate number, find
the duplicate one.

Note:
You must not modify the array (assume the array is read only).
You must use only constant, O(1) extra space.
Your runtime complexity should be less than O(n2).
There is only one duplicate number in the array, but it could be repeated more than once.
'''




# 用计数排序写的，不符合题目条件
class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        lst = [0] * (max(nums) + 1)
        # pass
        for s in nums:
            lst[s] += 1

        for a in range(len(lst)):
            if lst[a] > 1: return a

        return 1
