# coding=utf-8

'''
Given an integer array nums, find the sum of the elements between
indices i and j (i ≤ j), inclusive.

Example:
Given nums = [-2, 0, 3, -5, 2, -1]

sumRange(0, 2) -> 1
sumRange(2, 5) -> -1
sumRange(0, 5) -> -3
Note:
You may assume that the array does not change.
There are many calls to sumRange function.

'''

# 简单的累加就可以了，求范围和时拿两个点的值相减就行
# Beat 92.45%

class NumArray(object):
    def __init__(self, nums):
        """
        initialize your data structure here.
        :type nums: List[int]
        """
        n = len(nums)
        if n == 0: return
        self.ref = [0] * (n + 1)
        for i in xrange(1, n + 1):
            self.ref[i] = self.ref[i - 1] + nums[i - 1]

    def sumRange(self, i, j):
        """
        sum of elements nums[i..j], inclusive.
        :type i: int
        :type j: int
        :rtype: int
        """
        return self.ref[j + 1] - self.ref[i]



# Your NumArray object will be instantiated and called as such:
# numArray = NumArray(nums)
# numArray.sumRange(0, 1)
# numArray.sumRange(1, 2)
