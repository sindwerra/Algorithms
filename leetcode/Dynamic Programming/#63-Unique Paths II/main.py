# coding=utf-8

'''
Follow up for "Unique Paths":

Now consider if some obstacles are added to the grids.
How many unique paths would there be?

An obstacle and empty space is marked as 1 and 0 respectively in the grid.

For example,
There is one obstacle in the middle of a 3x3 grid as illustrated below.

[
  [0,0,0],
  [0,1,0],
  [0,0,0]
]
The total number of unique paths is 2.

Note: m and n will be at most 100.
'''

# 基本上和62没区别，只需要注意有障碍的地方有个判断就行了
# 另外初始化的时候值要设置好，Beat 87.44%

class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        n = len(obstacleGrid)
        if n == 0: return 0
        m = len(obstacleGrid[0])
        if m == 0: return 0

        # 起始点就有可能有障碍，这样直接返回0了

        if obstacleGrid[0][0] == 1: return 0

        ref = [([0] * m) for _ in xrange(n)]
        ref[0][0] = 1

        # 没障碍时，左边和顶边点的值随之前点的值，有障碍直接设置为0

        for a in xrange(1, n):
            if obstacleGrid[a][0] != 1:
                ref[a][0] = ref[a - 1][0]
            else:
                ref[a][0] = 0

        for b in xrange(1, m):
            if obstacleGrid[0][b] != 1:
                ref[0][b] = ref[0][b - 1]
            else:
                ref[0][b] = 0

        # 动归主体，添加了一个判断而已

        for row in xrange(1, n):
            for col in xrange(1, m):
                if obstacleGrid[row][col] == 1:
                    ref[row][col] = 0
                else:
                    ref[row][col] = ref[row - 1][col] + ref[row][col - 1]

        return ref[n - 1][m - 1]
