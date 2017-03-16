# coding=utf-8

'''
A robot is located at the top-left corner of a m x n grid
(marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time.
The robot is trying to reach the bottom-right corner of the grid
(marked 'Finish' in the diagram below).

How many possible unique paths are there?


Above is a 3 x 7 grid. How many possible unique paths are there?

Note: m and n will be at most 100.
'''

# 基本可以说是最简单的二维动归题了，没有任何特殊思路
# Beat 83.5%

class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        if m == 0 or n == 0: return 0
        res = [([0] * m) for _ in xrange(n)]
        res[0] = [1] * m
        for a in xrange(1, n):
            res[a][0] = 1

        for row in xrange(1, n):
            for col in xrange(1, m):
                res[row][col] = res[row - 1][col] + res[row][col - 1]

        return res[n - 1][m - 1]
