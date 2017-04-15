# coding=utf-8

'''
Follow up for N-Queens problem.

Now, instead outputting board configurations, return the total number of distinct solutions.
'''

'''
就是第一个一样的方法做的，没有画棋盘的函数了而已，不过肯定有特殊的针对方法做
Beat 43.59%
公司：Zenefits
'''

class Solution(object):
    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: int
        """
        res, tmp = [0], []
        self.helper(n, tmp, res, 0)
        return res[0]
    
    def helper(self, n, tmp, res, count):
        if count == n:
            res[0] += 1
            return
        
        for i in xrange(n):
            if not self.isValid(tmp, count, i):
                continue
            tmp.append(i)
            self.helper(n, tmp, res, count + 1)
            tmp.pop()
    
    def isValid(self, tmp, count, i):
        for row, col in enumerate(tmp):
            if row == count or col == i:
                return False
            if row - col == count - i:
                return False
            if row + col == count + i:
                return False
        return True
