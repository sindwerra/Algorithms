# coding=utf-8

'''
Given a matrix of m x n elements (m rows, n columns),
return all elements of the matrix in spiral order.

For example,
Given the following matrix:

[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
You should return [1,2,3,6,9,8,7,4,5].
'''

# 此题思路问题不大，关键是三类特殊边界情况很蛋疼，
# 考虑最后中心只剩一排，只剩一行，或者只剩一个点三种情况如何处理
# Beat 29%

class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        res = []
        if len(matrix) == 0: return res

        row_lf, col_lf = 0, 0
        row_rt, col_rt = len(matrix) - 1, len(matrix[0]) - 1
        while row_lf < row_rt and col_lf < col_rt:
            res += matrix[row_lf][col_lf:col_rt]

            for b in xrange(row_lf, row_rt):
                res.append(matrix[b][col_rt])

            res += matrix[row_rt][col_rt:col_lf:-1]

            for d in xrange(row_rt, row_lf, -1):
                res.append(matrix[d][col_lf])

            row_lf += 1
            col_lf += 1
            row_rt -= 1
            col_rt -= 1

# 处理特殊情况的代码

        if row_lf == row_rt:
            for s in xrange(col_lf, col_rt + 1):
                res.append(matrix[row_lf][s])
        elif col_lf == col_rt:
            for s in xrange(row_lf, row_rt + 1):
                res.append(matrix[s][col_lf])



        return res
