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

'''
用set来检查对角线攻击的方法
Beat 94.36%
'''

class Solution(object):
    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: int
        """
        col, left_dia, right_dia = set([]), set([]), set([])
        count = [0]
        return self.helper(0, count, n, col, left_dia, right_dia)

    def helper(self, row, count, n, col, left_dia, right_dia):
        for i in xrange(n):
            if i in col:
                continue
            if (row - i) in left_dia:
                continue
            if (row + i) in right_dia:
                continue
            if row >= n - 1:
                count[0] += 1
            else:
                col.add(i)
                left_dia.add(row - i)
                right_dia.add(row + i)
                self.helper(row + 1, count, n, col, left_dia, right_dia)
                col.remove(i)
                left_dia.remove(row - i)
                right_dia.remove(row + i)
        
        return count[0]