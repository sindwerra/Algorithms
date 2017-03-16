# coding=utf-8

'''
Given a m x n matrix, if an element is 0,
set its entire row and column to 0. Do it in place.
'''

# 建立一个同规模的参考矩阵，将所有等于0的位置标记下来，用以在遍历时判断
# Beat 41.29%

class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        m = len(matrix[0])
        ref = [([False] * m) for _ in xrange(n)]
        for index in xrange(n):
            for s in xrange(m):
                if matrix[index][s] == 0:
                    ref[index][s] = True

        for a in xrange(n):
            for b in xrange(m):
                if matrix[a][b] == 0 and ref[a][b] == True:
                    matrix[a] = [0] * m
                    for i in xrange(n):
                        matrix[i][b] = 0
