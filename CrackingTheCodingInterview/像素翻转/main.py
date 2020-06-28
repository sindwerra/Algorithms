# coding=utf-8

'''
有一副由NxN矩阵表示的图像，这里每个像素用一个int表示，请编写一个算法，
在不占用额外内存空间的情况下(即不使用缓存矩阵)，将图像顺时针旋转90度。
给定一个NxN的矩阵，和矩阵的阶数N,请返回旋转后的NxN矩阵,保证N小于等于500，
图像元素小于等于256。
测试样例：
[[1,2,3],[4,5,6],[7,8,9]],3
返回：[[7,4,1],[8,5,2],[9,6,3]]
'''

# -*- coding:utf-8 -*-
class Transform:
    def transformImage(self, matrix, n):
        # write code here
        st, ed, n = 0, len(matrix) - 1, len(matrix) - 1
        if n <= 0: return matrix
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
        return matrix
