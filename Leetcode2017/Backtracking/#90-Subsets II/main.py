# coding=utf-8

'''
Given a collection of integers that might contain duplicates, nums,
return all possible subsets.

Note: The solution set must not contain duplicate subsets.

For example,
If nums = [1,2,2], a solution is:

[
  [2],
  [1],
  [1,2,2],
  [2,2],
  [1,2],
  []
]
'''

'''
九章介绍的查重的方法，重复数只能连续取不能跳跃取
Beat 64.95%
公司：Facebook
'''

class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        tmp, res = [], []
        self.helper(0, len(nums), tmp, res, nums)
        return res

    def helper(self, start, end, tmp, res, nums):
        ref = tmp[:]
        res.append(ref)

        if start == end:
            return

        for i in xrange(start, end):
            if i - 1 >= 0 and nums[i - 1] == nums[i] and i > start:
                continue
            tmp.append(nums[i])
            self.helper(i + 1, end, tmp, res, nums)
            tmp.pop()
