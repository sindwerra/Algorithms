# coding=utf-8

'''
Given an unsorted integer array, find the first 
missing positive integer.

For example,
Given [1,2,0] return 3,
and [3,4,-1,1] return 2.

Your algorithm should run in O(n) time and uses 
constant space.
'''

'''
比想象中好搞一点，另外发现了一个python换值的漏洞
Beat 63.08%
'''

class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        start = 0
        count = 0

        while start < n:
            if nums[start] != start + 1 and 0 < nums[start] <= n:
                if nums[start] != nums[nums[start] - 1]:
                    tmp = nums[nums[start] - 1]
                    nums[nums[start] - 1] = nums[start]
                    nums[start] = tmp
                    continue
            start += 1

        
        for i in xrange(n):
            if nums[i] != i + 1:
                return i + 1
        
        return n + 1