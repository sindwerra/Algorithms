# coding=utf-8

'''
Given an integer n, generate a square matrix filled with
elements from 1 to n2 in spiral order.

For example,
Given n = 3,

You should return the following matrix:
[
 [ 1, 2, 3 ],
 [ 8, 9, 4 ],
 [ 7, 6, 5 ]
]
'''

# 基本跟54一样的套路，多一个count给各个元素赋值即可

class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        res = [([0] * n) for _ in xrange(n)]

        row_lf, col_lf = 0, 0
        row_rt, col_rt = n - 1, n - 1
        count = 1
        while row_lf < row_rt and col_lf < col_rt:
            for a in xrange(col_lf, col_rt):
                res[row_lf][a] = count
                count += 1
            for b in xrange(row_lf, row_rt):
                res[b][col_rt] = count
                count += 1
            for c in xrange(col_rt, col_lf, -1):
                res[row_rt][c] = count
                count += 1
            for d in xrange(row_rt, row_lf, -1):
                res[d][col_lf] = count
                count += 1

            row_lf += 1
            row_rt -= 1
            col_lf += 1
            col_rt -= 1

        if row_lf == row_rt:
            for s in xrange(col_lf, col_rt + 1):
                res[row_lf][s] = count
                count += 1
        elif col_lf == col_rt:
            for j in xrange(row_lf, row_rt + 1):
                res[j][col_lf] = count
                count += 1

        return res
