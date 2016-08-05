# coding=utf-8

# '''
# Given an array of size n, find the majority element.
# The majority element is the element that appears more than ⌊ n/2 ⌋ times.
#
# You may assume that the array is non-empty and the majority element
# always exist in the array.
# '''

# 怎么用分治算法做这道题？

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        store = {}
        if len(nums) == 1: return nums[0]
        count = len(nums) / 2
        for s in nums:
            if store.has_key(s):
                store[s] += 1
                if store[s] > count: return s
            else: store[s] = 1

        return 0
