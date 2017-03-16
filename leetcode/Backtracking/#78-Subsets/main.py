# coding=utf-8

'''
Given a set of distinct integers, nums, return all possible subsets.

Note: The solution set must not contain duplicate subsets.

For example,
If nums = [1,2,3], a solution is:

[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]
'''

'''
还是回溯，感觉也没什么好讲的...一个是n个阶乘，一个是一个n的阶乘，
关键都在于递归调用的起始点选择上，Beat 51.97%
'''

class Solution(object):
    def SS(self, st, ed, lst, nums, tmp):
        if st == ed:
            return
        for i in xrange(st, ed):
            tmp.append(nums[i])
            self.SS(i + 1, ed, lst, nums, tmp)
            ref = tmp[:]
            lst.append(ref)
            tmp.pop()

    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res, tmp = [], []
        self.SS(0, len(nums), res, nums, tmp)
        return res + [[]]
