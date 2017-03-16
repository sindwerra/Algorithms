# coding=utf-8

'''
动归算法，Beat 74.02%
'''

class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n <= 1:
            nums = [0] + nums
            return nums[-1]
        res = []
        cur = 0
        for s in range(n):
            a = max(nums[s], nums[s] + cur)
            res.append(a)
            cur = a
        return max(res)
