# coding=utf-8

'''
Given a sorted array, remove the duplicates in place such that each element
appear only once and return the new length.

Do not allocate extra space for another array, you must do this in place
with constant memory.

For example,
Given input array nums = [1,1,2],

Your function should return length = 2, with the first two elements of
nums being 1 and 2 respectively. It doesn't matter what you leave beyond
the new length.
'''

'''
Beat 20.22%
'''

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        st, ed = 0, 1
        n = len(nums)
        while ed <= n - 1:
            if nums[st] == nums[ed]:
                ed -= 1
                n -= 1
                del nums[ed + 1]
                ed += 1
            else:
                st += 1
                ed += 1
        return n
