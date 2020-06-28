# coding=utf-8

'''
Note: This is an extension of House Robber.

After robbing those houses on that street, the thief has found himself 
a new place for his thievery so that he will not get too much attention. 
This time, all houses at this place are arranged in a circle. 
That means the first house is the neighbor of the last one. 
Meanwhile, the security system for these houses remain the same as 
for those in the previous street.

Given a list of non-negative integers representing the amount of 
money of each house, determine the maximum amount of money you can 
rob tonight without alerting the police.
'''

'''
就是照九章的做法，既然循环，就把第一个不要，再把最后一个不要，这样就拆成两个
非循环的做两次动态规划就行了
Beat 77.32%
公司：Microsoft
'''

class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        
        n = len(nums)
        
        if n == 1:
            return nums[0]
        
        ref = [0] * n
        ref[1] = nums[1]
        for i in xrange(2, n):
            ref[i] = max(ref[i - 1], ref[i - 2] + nums[i])
        
        result = ref[-1]

        ref[0] = 0
        ref[1] = nums[0]
        for i in xrange(1, n - 1):
            ref[i + 1] = max(ref[i], ref[i - 1] + nums[i])
        
        return max(result, ref[-1])
