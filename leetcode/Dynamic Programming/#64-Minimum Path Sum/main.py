# coding=utf-8

'''
Given a m x n grid filled with non-negative numbers,
find a path from top left to bottom right which minimizes the
sum of all numbers along its path.

Note: You can only move either down or right at any point in time.
'''

# 跟牛客网那个题一样的，Beat 94.5%

class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        # 一堆狗判断条件

        n = len(grid)
        if n == 0: return 0
        m = len(grid[0])
        if m == 0: return 0

        # 初始化参考矩阵

        ref = [([0] * m) for _ in xrange(n)]
        ref[0][0] = grid[0][0]
        for a in xrange(1, n):
            ref[a][0] = ref[a - 1][0] + grid[a][0]
        for b in xrange(1, m):
            ref[0][b] = ref[0][b - 1] + grid[0][b]

        # DP部分

        for c in xrange(1, n):
            for d in xrange(1, m):
                ref[c][d] = min(ref[c - 1][d], ref[c][d - 1]) + grid[c][d]
        return ref[n - 1][m - 1]
