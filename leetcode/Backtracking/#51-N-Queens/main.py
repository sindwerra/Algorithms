# coding=utf-8

'''
The n-queens puzzle is the problem of placing n queens on an n×n chessboard such that no two queens attack 
each other.



Given an integer n, return all distinct solutions to the n-queens puzzle.

Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both 
indicate a queen and an empty space respectively.

For example,
There exist two distinct solutions to the 4-queens puzzle:

[
 [".Q..",  // Solution 1
  "...Q",
  "Q...",
  "..Q."],

 ["..Q.",  // Solution 2
  "Q...",
  "...Q",
  ".Q.."]
]
'''

'''
一个经典问题，根据九章视频做的，还是一样套回溯法的模板做，不过需要一个检测对角线攻击的函
数和一个画棋盘的函数，另外行列皇后放的位置存储在tmp列表里，index代表行数，值代表列数。
这里拿的最容易理解的版本
Beat 53.67%
'''

class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        res, tmp = [], []
        self.helper(n, tmp, res, 0)
        return res
    
    def helper(self, n, tmp, res, count):
        if len(tmp) == n:
            res.append(self.drawBoard(tmp, n))
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
    
    def drawBoard(self, location, n):
        res = []
        for i in xrange(n):
            tmp = ''
            for j in xrange(n):
                if location[i] == j:
                    tmp += 'Q'
                    continue
                tmp += '.'
            res.append(tmp)
        return res
        