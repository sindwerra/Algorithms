# coding=utf-8

# '''
# Given an array containing n distinct numbers taken from 0, 1, 2, ..., n,
# find the one that is missing from the array.
#
# For example,
# Given nums = [0, 1, 3] return 2.
#
# Note:
# Your algorithm should run in linear runtime complexity. Could you implement
# it using only constant extra space complexity?
# '''

# 计数排序哈哈哈哈哈哈，这个题没有用标签里的bit manipulation方法做，这种固定正数一定范围
# 内的找数，排序用计数排序实在太方便，Beat 43.01%

class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        bucket = [0] * (len(nums) + 1)
        for s in nums:
            bucket[s] = 1

        return bucket.index(0)

'''
另外一种做法，求1到n的和然后减去当前数组的和就是丢掉的那个数字了
'''

class Solution(object):
    def missingNumber(self, A):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(A)
        result = 0
        for i in xrange(1, n + 1):
            result += i
        return result - sum(A)
