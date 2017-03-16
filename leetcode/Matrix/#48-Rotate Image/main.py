# coding=utf-8

'''
You are given an n x n 2D matrix representing an image.

Rotate the image by 90 degrees (clockwise).

Follow up:
Could you do this in-place?
'''

# 要想in-place必须要一直用row和col变量来改变当前点
# 顺时针90度的规律就是row = col， col = n - row
# 边际条件和变量非常多，要注意区分
# Beat 98.03%

class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        st, ed, n = 0, len(matrix) - 1, len(matrix) - 1
        if n <= 0: return
        while st < ed:
            for s in xrange(st, ed):
                row, col = st, s
                tmp = matrix[row][col]
                for times in xrange(4):
                    matrix[col][n - row], tmp = tmp, matrix[col][n - row]
                    a, b = row, col
                    row, col = b, n - a
            st += 1
            ed -= 1
