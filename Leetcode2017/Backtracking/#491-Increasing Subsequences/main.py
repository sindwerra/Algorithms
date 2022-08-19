# coding=utf-8

'''
Given an integer array, your task is to find all the different possible increasing 
subsequences of the given array, and the length of an increasing subsequence 
should be at least 2 .

Example:
Input: [4, 6, 7, 7]
Output: [[4, 6], [4, 7], [4, 6, 7], [4, 6, 7, 7], [6, 7], [6, 7, 7], [7,7], [4,7,7]]
Note:
The length of the given array will not exceed 15.
The range of integer in the given array is [-100,100].
The given array may contain duplicates, and two equal integers should also 
be considered as a special case of increasing sequence.
'''

'''
这题注意下查重方式就行，结果的搜集是subset的形式，查重是用的permutation的方式
做这题的时候脑子很清晰，所以bug free了
Beat 96.07%
公司：Yahoo
'''

class Solution(object):
    def findSubsequences(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        tmp, res = [], []
        self.helper(0, len(nums), tmp, res, nums)
        return res

    def helper(self, start, end, tmp, res, nums):
        if len(tmp) >= 2:
            ref = tmp[:]
            res.append(ref)
        
        if start >= end:
            return 

        store = {}
        for i in xrange(start, end):
            if (not tmp or tmp[-1] <= nums[i]) and nums[i] not in store:
                store[nums[i]] = 1
                tmp.append(nums[i])
                self.helper(i + 1, end, tmp, res, nums)
                tmp.pop()
