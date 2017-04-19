# coding=utf-8

'''
Given an array nums, write a function to move all 0's to the end of it while maintaining the 
relative order of the non-zero elements.

For example, given nums = [0, 1, 0, 3, 12], after calling your function, nums should be [1, 3, 12, 0, 0].

Note:
You must do this in-place without making a copy of the array.
Minimize the total number of operations.
'''

'''
思想是很类似快排的partition的，双快慢指针从开始点出发扫就行了
Beat 59.00%
公司：Bloomberg, Facebook
'''

class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        tail, head = 0, 1
        n = len(nums)

        while head < n:
            while head < n and nums[head] == 0:
                head += 1
            while tail < head and nums[tail] != 0:
                tail += 1
            if tail < head and head < n:
                nums[tail], nums[head] = nums[head], nums[tail]
            tail += 1
            head += 1