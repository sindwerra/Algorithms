# coding=utf-8

'''
Given an integer matrix, find the length of the longest increasing path.

From each cell, you can either move to four directions:
left, right, up or down. You may NOT move diagonally or
move outside of the boundary (i.e. wrap-around is not allowed).

Example 1:

nums = [
  [9,9,4],
  [6,6,8],
  [2,1,1]
]
Return 4
The longest increasing path is [1, 2, 6, 9].

Example 2:

nums = [
  [3,4,5],
  [3,2,6],
  [2,2,1]
]
Return 4
The longest increasing path is [3, 4, 5, 6].
Moving diagonally is not allowed.
'''

# 动归里面很难的题了，实际上和北大的动归视频里面的滑雪题一样
# Beat 87.06%

class Solution(object):
    def longestIncreasingPath(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        if len(matrix) == 0: return 0   # 空矩阵的处理

        row, col = len(matrix), len(matrix[0])
        L = [([1] * col) for _ in xrange(row)]  # 参考的距离矩阵

        # 存放高度和坐标到一个list中

        ref = []
        for s in xrange(row):
            for j in xrange(col):
                ref.append([matrix[s][j], (s, j)])

        ref.sort()      # 按照高度排序所有点

        # 将排好序的点按照从低到高的顺序遍历，并逐渐增高四周点高度

        for lst in ref:
            h = lst[0]
            c, l = lst[1][0], lst[1][1]
            if c - 1 >= 0 and matrix[c - 1][l] > h:
                L[c - 1][l] = max(L[c - 1][l], L[c][l] + 1)
            if c + 1 <= row - 1 and matrix[c + 1][l] > h:
                L[c + 1][l] = max(L[c + 1][l], L[c][l] + 1)
            if l - 1 >= 0 and matrix[c][l - 1] > h:
                L[c][l - 1] = max(L[c][l - 1], L[c][l] + 1)
            if l + 1 <= col - 1 and matrix[c][l + 1] > h:
                L[c][l + 1] = max(L[c][l + 1], L[c][l] + 1)

        # 找出路径矩阵中的最大值

        res = 0
        for num in L:
            tmp = max(num)
            if res < tmp:
                res = tmp
        return res
