# coding=utf-8

'''
Given a collection of numbers that might contain duplicates,
return all possible unique permutations.

For example,
[1,1,2] have the following unique permutations:
[
  [1,1,2],
  [1,2,1],
  [2,1,1]
]
'''

'''
这种backtracking真的做的都没感觉，还需要很多练习啊...
Beat 92.30%
公司：LinkedIn, Microsoft
'''

class Solution(object):
    def permuteUnique(self, nums):
        # write your code here
        nums.sort()
        res = []
        self.helper(0, len(nums), res, nums)
        return res

    def helper(self, start, end, res, nums):
        if start >= end - 1:
            ref = nums[:]
            res.append(ref)
            return

        store = {}

        for i in xrange(start, end):
            if store.has_key(nums[i]):
                continue
            store[nums[i]] = 1
            nums[i], nums[start] = nums[start], nums[i]
            self.helper(start + 1, end, res, nums)
            nums[i], nums[start] = nums[start], nums[i]
