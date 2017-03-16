# coding=utf-8

'''
Given a n x n matrix where each of the rows and columns are sorted in
ascending order, find the kth smallest element in the matrix.

Note that it is the kth smallest element in the sorted order, not the
kth distinct element.

Example:

matrix = [
   [ 1,  5,  9],
   [10, 11, 13],
   [12, 13, 15]
],
k = 8,

return 13.
Note:
You may assume k is always valid, 1 ≤ k ≤ n2.
'''

'''
按照九章强化班的思维做的，相当于每一次的最小值决出之后，最小值所在位置的
下方和右方的值要进入这个堆，每次维护这个堆弹出来的就是最小值，但是此处
initialize这个参考矩阵时的时间复杂度已经超过主算法了，应该是可以优化的
Beat 27.72%
公司：Google, Twitter
'''

class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        n = len(matrix)
        if not n:
            return 0

        m = len(matrix[0])
        if not m:
            return 0

        heap = []
        ref = [([0] * m) for _ in range(n)]

        store = {}
        row, col = 0, 0
        res = matrix[0][0]
        for i in xrange(k):
            if i:
                res, node = heapq.heappop(heap)
                row, col = node

            if row + 1 < n and not ref[row + 1][col]:
                heapq.heappush(heap, [matrix[row + 1][col], [row + 1, col]])
                ref[row + 1][col] = 1
            if col + 1 < m and not ref[row][col + 1]:
                heapq.heappush(heap, [matrix[row][col + 1], [row, col + 1]])
                ref[row][col + 1] = 1

        return res

            
