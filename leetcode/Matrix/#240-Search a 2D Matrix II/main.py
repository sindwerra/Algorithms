# coding=utf-8

'''Write an efficient algorithm that searches for a value in an m x n matrix.
This matrix has the following properties:

Integers in each row are sorted in ascending from left to right.
Integers in each column are sorted in ascending from top to bottom.
For example,

Consider the following matrix:

[
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]
Given target = 5, return true.

Given target = 20, return false.
'''

# 根据牛客网的教程写的，从右上角顶点找起，这个题和Search 2D matrix I不一样
# 条件里有保证了从上到下，从左到右都是升序，如果没有这两个条件不能这样做

class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        bot_bound = len(matrix) - 1
        row, col = 0, len(matrix[0]) - 1
        while col >= 0 and row <= bot_bound:
            if matrix[row][col] < target:
                row += 1
            elif matrix[row][col] > target:
                col -= 1
            else:
                return True

        return False
