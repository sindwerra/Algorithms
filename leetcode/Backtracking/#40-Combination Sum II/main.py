# coding=utf-8

'''
Given a collection of candidate numbers (C) and a target number (T), find all unique combinations 
in C where the candidate numbers sums to T.

Each number in C may only be used once in the combination.

Note:
All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.
For example, given candidate set [10, 1, 2, 7, 6, 1, 5] and target 8, 
A solution set is: 
[
  [1, 7],
  [1, 2, 5],
  [2, 6],
  [1, 1, 6]
]
'''

'''
没什么好说的，跟第一个基本是一样的，只要加一个st == ed的判断就行了，因为每个数只能选一次
Beat 39.79%
公司：Snapchat
'''

class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res, tmp = [], []
        self.helper(candidates, 0, len(candidates), tmp, res, target)
        return res
        
    def helper(self, candidates, st, ed, tmp, res, target):
        if target == 0:
            ref = tmp[:]
            res.append(ref)
            return 
        
        if target < 0 or st == ed:
            return 
        
        for i in xrange(st, ed):
            if i - 1 >= 0 and i > st and candidates[i] == candidates[i - 1]:
                continue
            tmp.append(candidates[i])
            self.helper(candidates, i + 1, ed, tmp, res, target - candidates[i])
            tmp.pop()
        

'''
第二个版本，看了九章的答案知道的，一行当前值的判断语句，速度从15%左右变到90%左右了
'''   

class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()
        res, tmp = [], []
        self.helper(candidates, 0, len(candidates), tmp, res, target)
        return res
        
    def helper(self, candidates, st, ed, tmp, res, target):
        if target == 0:
            ref = tmp[:]
            res.append(ref)
            return 
        
        if target < 0 or st == ed:
            return 
        
        for i in xrange(st, ed):
            if candidates[i] > target:
                break
            if i - 1 >= 0 and i > st and candidates[i] == candidates[i - 1]:
                continue
            tmp.append(candidates[i])
            self.helper(candidates, i + 1, ed, tmp, res, target - candidates[i])
            tmp.pop()