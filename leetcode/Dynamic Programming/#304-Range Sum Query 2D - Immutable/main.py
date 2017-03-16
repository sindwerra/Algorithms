# coding=utf-8

'''
Given a 2D matrix matrix, find the sum of the elements inside the
rectangle defined by its upper left corner (row1, col1) and lower
right corner (row2, col2).

Range Sum Query 2D
The above rectangle (with the red border) is defined by
(row1, col1) = (2, 1) and (row2, col2) = (4, 3), which contains sum = 8.

Example:
Given matrix = [
  [3, 0, 1, 4, 2],
  [5, 6, 3, 2, 1],
  [1, 2, 0, 1, 5],
  [4, 1, 0, 1, 7],
  [1, 0, 3, 0, 5]
]

sumRegion(2, 1, 4, 3) -> 8
sumRegion(1, 1, 2, 2) -> 11
sumRegion(1, 2, 2, 4) -> 12
Note:
You may assume that the matrix does not change.
There are many calls to sumRegion function.
You may assume that row1 ≤ row2 and col1 ≤ col2.
'''

# 速度太慢

class NumMatrix(object):
    def __init__(self, matrix):
        """
        initialize your data structure here.
        :type matrix: List[List[int]]
        """
        row = len(matrix)
        if row == 0: return
        col = len(matrix[0])
        if col == 0: return

        self.store = [([0] * (col + 1)) for _ in xrange(row + 1)]
        self.ref = [([0] * (col + 1)) for _ in xrange(row + 1)]

        for i in xrange(row):
            for j in xrange(col):
                self.store[i][j] = matrix[i][j]
                self.ref[i][j] = matrix[i][j]

        for r in xrange(row):
            for c in xrange(1, col):
                self.store[r][c] += self.store[r][c - 1]


    def sumRegion(self, row1, col1, row2, col2):
        """
        sum of elements matrix[(row1,col1)..(row2,col2)], inclusive.
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        res = 0
        for s in xrange(row1, row2 + 1):
            res += (self.store[s][col2] - self.store[s][col1] + self.ref[s][col1])
        return res
