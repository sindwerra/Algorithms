# coding=utf-8

'''
Given a matrix of M x N elements (M rows, N columns), return all elements of the matrix in diagonal order as shown in the below image.

Example:
Input:
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
Output:  [1,2,4,7,5,3,6,8,9]
Explanation:

'''

'''
此题撞墙情况特别多，奇数轮和偶数轮坐标的移位都是有两种情况的，另外对角线打印的次数适合行列数总和有关的
Beat 87.91%
公司：Google
'''

class Solution(object):
    def findDiagonalOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        n = len(matrix)
        if not n:
            return []

        if n == 1:
            return matrix[0]
        
        m = len(matrix[0])
        if not m:
            return []

        if m == 1:
            return [x[0] for x in matrix]

        result = []
        cursor = [0, 0]

        for time in xrange(n + m - 1):
            if time % 2 == 1:
                while cursor[0] + 1 < n and cursor[1] - 1 >= 0:
                    result.append(matrix[cursor[0]][cursor[1]])
                    cursor[0] += 1
                    cursor[1] -= 1
                result.append(matrix[cursor[0]][cursor[1]])
                if cursor[0] + 1 < n:
                    cursor[0] += 1
                else:
                    cursor[1] += 1
            else:
                while cursor[0] - 1 >= 0 and cursor[1] + 1 < m:
                    result.append(matrix[cursor[0]][cursor[1]])
                    cursor[0] -= 1
                    cursor[1] += 1
                result.append(matrix[cursor[0]][cursor[1]])
                if cursor[1] + 1 < m:
                    cursor[1] += 1
                else:
                    cursor[0] += 1

        return result