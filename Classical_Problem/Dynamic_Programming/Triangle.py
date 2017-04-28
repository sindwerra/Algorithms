# coding=utf-8

'''
Given a triangle, find the minimum path sum from top to bottom.
Each step you may move to adjacent numbers on the row below.

For example, given the following triangle
[
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]
The minimum path sum from top to bottom is 11 (i.e., 2 + 3 + 5 + 1 = 11).

Note:
Bonus point if you are able to do this using only O(n) extra space,
where n is the total number of rows in the triangle.
'''

# 北大算法的一个题，解决上没有难度，关键是实现O(n)的额外空间复杂度
# 需要用一个和三角矩阵的行数一样长度的list来存储值，每一行遍历完后更新list
# Beat 97.27%

class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        n = len(triangle)
        ref = [0] * len(triangle)          # 参考list
        ref[0] = triangle[0][0]
        for row in xrange(1, n):
            m = len(triangle[row])         # 当前行长度
            tmp = []                       # 临时存储值list
            for col in xrange(m):
                q = sys.maxint
                if col - 1 >= 0:
                    q = min(q, ref[col - 1])
                if col <= m - 2:
                    q = min(q, ref[col])
                tmp.append(q + triangle[row][col])
            ref[:m] = tmp                  # 将临时list移入参考list中
        return min(ref)
