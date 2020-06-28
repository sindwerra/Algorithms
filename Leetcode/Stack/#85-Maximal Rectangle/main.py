# coding=utf-8

'''
Given a 2D binary matrix filled with 0's and 1's, find the largest rectangle 
containing only 1's and return its area.

For example, given the following matrix:

1 0 1 0 0
1 0 1 1 1
1 1 1 1 1
1 0 0 1 0
Return 6.
'''

'''
这题就是上一道的follow up，主要就是要想出来从行来遍历然后积累1的个数从而把一个二维问题
转化为之前的一维问题来解决，临时的一维数组建好之后只要调用之前的函数就可以解决问题了
Beat 38.65%
公司：Facebook
'''

class Solution(object):
    def maximalRectangle(self, matrix):
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

        tmp = [0] * m
        result = -sys.maxint

        for i in xrange(n):
            for j in xrange(m):
                tmp[j] = tmp[j] + int(matrix[i][j]) if int(matrix[i][j]) == 1 else 0
            result = max(result, self.largestRectangleArea(tmp, m))
        
        return result

    def largestRectangleArea(self, heights, n):
        if not heights:
            return 0

        stack = [0]
        result = heights[0]

        for i in xrange(1, n):
            if heights[i] <= heights[stack[-1]]:
                while stack and heights[stack[-1]] >= heights[i]:
                    tmp = stack.pop()
                    if stack:
                        result = max(result, heights[tmp] * (i - stack[-1] - 1))
                    else:
                        result = max(result, heights[tmp] * i)
            stack.append(i)
        
        while stack:
            tmp = stack.pop()
            if stack:
                result = max(result, heights[tmp] * (n - 1 - stack[-1]))
            else:
                result = max(result, heights[tmp] * n)
            
        return result