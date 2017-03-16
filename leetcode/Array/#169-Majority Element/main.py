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


'''
Moore's voter Algorithm做这道题，并且输入保证有一个majorityElement
所以只需要algorithm的第一个步骤就行了
Beat 78.97%
'''

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        mj_index, count = 0, 0
        n = len(nums)
        for s in range(n):
            if nums[s] == nums[mj_index]:
                count += 1
            else:
                count -= 1
                if not count:
                    mj_index = s
                    count = 1
        return nums[mj_index]
