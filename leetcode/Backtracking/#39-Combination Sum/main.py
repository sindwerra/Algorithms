# coding=utf-8

'''
Given a set of candidate numbers (C) and a target number (T),
find all unique combinations in C where the candidate numbers sums to T.

The same repeated number may be chosen from C unlimited number of times.

Note:
All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.
For example, given candidate set [2, 3, 6, 7] and target 7,
A solution set is:
[
  [7],
  [2, 2, 3]
]
'''

'''
回溯法的例子，主要是要理解递归导致的范围变化以及判断条件，先排序预处理candidate数组
Beat 93.25%
'''

class Solution(object):
    def CS(self, base, tgt, lst, ref, tmp, depth):
        '''
        base: value already calculated
        tgt: target number
        lst: result List
        ref: candidates List
        tmp: one answer
        depth: 到了第几个数
        '''
        if base == tgt:
            a = tmp[:]
            lst.append(a)
            return

        for i in xrange(depth, len(ref)):
            if base + ref[i] <= tgt:
                tmp.append(ref[i])
                self.CS(base + ref[i], tgt, lst, ref, tmp, i)
                tmp.pop()

    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()
        res, tmp = [], []
        self.CS(0, target, res, candidates, tmp, 0)
        return res

'''
添加了查重的语句，leetcode本身的代码就有问题，所以这个才是正确答案
'''

class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()
        res, tmp = [], []
        self.helper(candidates, res, target, tmp, 0, len(candidates))
        return res
        
    def helper(self, candidates, res, target, tmp, st, ed):
        if target == 0:
            ref = tmp[:]
            res.append(ref)
            return 
        
        if target < 0:
            return 
        
        for i in xrange(st, ed):
            if i - 1 >= 0 and i > st and candidates[i] == candidates[i - 1]:
                continue
            tmp.append(candidates[i])
            self.helper(candidates, res, target - candidates[i], tmp, i, ed)
            tmp.pop()