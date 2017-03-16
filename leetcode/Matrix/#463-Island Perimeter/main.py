# coding=utf-8

'''
You are given a map in form of a two-dimensional integer grid where 1 represents land and 0 represents water. Grid cells are connected horizontally/vertically (not diagonally). The grid is completely surrounded by water, and there is exactly one island (i.e., one or more connected land cells). The island doesn't have "lakes" (water inside that isn't connected to the water around the island). One cell is a square with side length 1. The grid is rectangular, width and height don't exceed 100. Determine the perimeter of the island.

Example:

[[0,1,0,0],
 [1,1,1,0],
 [0,1,0,0],
 [1,1,0,0]]

Answer: 16
Explanation: The perimeter is the 16 yellow stripes in the image below:
'''

'''
逐个点检查就行，Beat 63.91%
公司：Google
'''

class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        res = 0
        row = len(grid)
        if row == 0: return 0
        col = len(grid[0])

        for i in range(row):
            for j in range(col):
                if grid[i][j]:
                    tmp = 0
                    if i - 1 < 0 or grid[i - 1][j] == 0:
                        tmp += 1
                    if j - 1 < 0 or grid[i][j - 1] == 0:
                        tmp += 1
                    if i + 1 > row - 1 or grid[i + 1][j] == 0:
                        tmp += 1
                    if j + 1 > col - 1 or grid[i][j + 1] == 0:
                        tmp += 1
                    res += tmp
        return res
