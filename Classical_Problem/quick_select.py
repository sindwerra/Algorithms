# coding=utf-8

'''
快速选择，和partition基本一样
'''

class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        n = len(nums)
        if k < 0 or k > n or n == 0:
            return -1

        return self.quickSelect(nums, 0, n - 1, k)
        
    def quickSelect(self, nums, start, end, k):
        if start >= end:
            return nums[end]
        
        left, right = start, end
        pivot = nums[left + (right - left) / 2]

        while left <= right:
            while left <= right and nums[left] > pivot:
                left += 1
            while left <= right and nums[right] < pivot:
                right -= 1
            if left <= right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1
        
        if start + k - 1 <= right:
            return self.quickSelect(nums, start, right, k)
        
        if start + k - 1 >= left:
            return self.quickSelect(nums, left, end, k - (left - start))
        
        return nums[right + 1]