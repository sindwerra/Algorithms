# coding=utf-8

'''
Given an unsorted array nums, reorder it in-place such that
nums[0] <= nums[1] >= nums[2] <= nums[3]....

For example, given nums = [3, 5, 2, 1, 6, 4], one possible
answer is [1, 6, 2, 5, 3, 4].
'''

'''
每个奇数位将相邻的三个元素最大的放在这里，每个偶数位将相邻的三个元素最小的放在这里
Beat 82.60%
公司：Google
'''

class Solution(object):
    def wiggleSort(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        if n == 2 and nums[0] > nums[1]:
            nums[0], nums[1] = nums[1], nums[0]
        for s in range(n - 1):
            if s % 2:
                if nums[s] < nums[s - 1]:
                    nums[s], nums[s - 1] = nums[s - 1], nums[s]
                if nums[s] < nums[s + 1]:
                    nums[s], nums[s + 1] = nums[s + 1], nums[s]
            else:
                if nums[s] > nums[s - 1]:
                    nums[s], nums[s - 1] = nums[s - 1], nums[s]
                if nums[s] > nums[s + 1]:
                    nums[s], nums[s + 1] = nums[s + 1], nums[s]

        
