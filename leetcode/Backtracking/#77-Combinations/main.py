# coding=utf-8

'''
Given two integers n and k, return all possible combinations of k numbers out of 1 ... n.

For example,
If n = 4 and k = 2, a solution is:

[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
]
'''

'''
还是照标准模板写就可以了，之前的不知道为什么TLE，应该有更巧的方法
Beat 13.77%
'''

class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        res, tmp = [], []
        self.helper(1, n + 1, tmp, res, 0, k)
        return res
        
    def helper(self, st, ed, tmp, res, count, limit):
        if count == limit:
            ref = tmp[:]
            res.append(ref)
            return 
        
        if st >= ed:
            return 
        
        for i in xrange(st, ed):
            tmp.append(i)
            self.helper(i + 1, ed, tmp, res, count + 1, limit)
            tmp.pop()
        
            
            
            
            