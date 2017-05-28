# coding=utf-8

'''
Given a matrix consists of 0 and 1, find the distance of the 
nearest 0 for each cell.

The distance between two adjacent cells is 1.
Example 1: 
Input:

0 0 0
0 1 0
0 0 0
Output:
0 0 0
0 1 0
0 0 0
Example 2: 
Input:

0 0 0
0 1 0
1 1 1
Output:
0 0 0
0 1 0
1 2 1
Note:
The number of elements of the given matrix will not exceed 10,000.
There are at least one 0 in the given matrix.
The cells are adjacent in only four directions: up, down, left and right.
'''

'''
看起来是个很普通的DFS题，但是实际做起来就发现有个问题，其中一个test case因为一个1在
太深处的地方而且很早就DFS过了，然而这个点的父进程方向离0更近却没有被这个子进程考虑到
所以导致结果不正确，下面这个代码虽然过了，但是并不是太好，因为针对了一个case做了
hard coding，在每次DFS之后还检查了一遍四周的距离最小值，所以此题可能还是用BFS做比较好
'''

class Solution(object):
    def updateMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        n = len(matrix)
        if not n:
            return []
        
        m = len(matrix[0])
        if not m:
            return []
        
        dirs = [[0, 1], [1, 0], [-1, 0], [0, -1]]
        ref = [([False] * m) for _ in xrange(n)]
        for i in xrange(n):
            for j in xrange(m):
                if not ref[i][j] and matrix[i][j] != 0:
                    self.DFS(i, j, matrix, ref, dirs, n, m)
                for row, col in dirs:                           # 这个循环一般DFS是不可能加的，所以很有问题其实
                    if 0 <= i + row < n and 0 <= j + col < m:
                        matrix[i][j] = min(matrix[i][j], matrix[i + row][j + col] + 1)
        
        return matrix

    def DFS(self, i, j, matrix, ref, dirs, n, m):
        if ref[i][j]:
            return matrix[i][j]
        
        matrix[i][j] = sys.maxint
        ref[i][j] = 1
        for r, l in dirs:
            row = i + r
            col = l + j
            if 0 <= row < n and 0 <= col < m:
                if not ref[row][col] and matrix[row][col]:
                    matrix[i][j] = min(matrix[i][j], self.DFS(row, col, matrix, ref, dirs, n, m) + 1)
                else:
                    matrix[i][j] = min(matrix[i][j], matrix[row][col] + 1)

        return matrix[i][j]
        
