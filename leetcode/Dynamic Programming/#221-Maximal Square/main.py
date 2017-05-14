# coding=utf-8

'''
Given a 2D binary matrix filled with 0's and 1's, find the largest square 
containing only 1's and return its area.

For example, given the following matrix:

1 0 1 0 0
1 0 1 1 1
1 1 1 1 1
1 0 0 1 0
Return 4.
'''

'''
以遍历的每个点当做一个正方形的右下角来记录当前点的最大正方形，这样发现之后左上，左边，上面的三个
点的数值可以影响到当前点的状态，所以去最小值加一即可，最后重新遍历整个参考矩阵找到那个最大值
Beat 87.47%
公司：Apple, Airbnb, Facebook
'''

class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        n = len(matrix)
        if not n:
            return 0

        m = len(matrix[0])
        if not m:
            return 0

        ref = [([0] * m) for _ in xrange(n)]

        for i in xrange(n):
            for j in xrange(m):
                if not i:
                    ref[i][j] = 1 if matrix[i][j] == '1' else 0
                elif not j:
                    ref[i][j] = 1 if matrix[i][j] == '1' else 0
                elif matrix[i][j] == '0':
                    ref[i][j] = 0
                else:
                    ref[i][j] = min(ref[i - 1][j - 1], ref[i - 1][j], ref[i][j - 1]) + 1
        
        result = -sys.maxint
        for i in xrange(n):
            result = max(result, max(ref[i]))
        
        return result * result