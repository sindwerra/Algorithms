# coding=utf-8

'''
Given an m x n matrix of positive integers representing the height of 
each unit cell in a 2D elevation map, compute the volume of water it 
is able to trap after raining.

Note:
Both m and n are less than 110. The height of each unit cell is 
greater than 0 and is less than 20,000.

Example:

Given the following 3x6 height map:
[
  [1,4,3,1,3,2],
  [3,2,1,3,2,4],
  [2,3,3,2,3,1]
]

Return 4.
'''

'''
这个题是个BFS然后用最小堆来代替队列辅助BFS进行，首先需要对四壁进行遍历并把
四壁的下标和高度一起扔进堆里面，此后每一次遍历都从堆里面找最小高度出来通过
最小高度往四周扫描，其中扫描到的值如果大于弹出来的点则无法灌水，但是此点
还是要放进堆中，max函数那一行就是把低于和高于两种情况压缩了
Beat 71.23%
公司：Google, Twitter
'''

class Solution(object):
    def trapRainWater(self, heightMap):
        """
        :type heightMap: List[List[int]]
        :rtype: int
        """
        n = len(heightMap)
        if not n:
            return 0
        m = len(heightMap[0])
        if not m:
            return 0
        
        ref = [([0] * m) for _ in range(n)]
        heap = []

        for i in xrange(n):
            heapq.heappush(heap, [heightMap[i][0], [i, 0]])
            heapq.heappush(heap, [heightMap[i][m - 1], [i, m - 1]])
            ref[i][0] = 1
            ref[i][m - 1] = 1
        
        for i in xrange(1, m - 1):
            heapq.heappush(heap, [heightMap[0][i], [0, i]])
            heapq.heappush(heap, [heightMap[n - 1][i], [n - 1, i]])
            ref[0][i] = 1
            ref[n - 1][i] = 1
        
        result = 0
        dirs = [[0, 1], [1, 0], [-1, 0], [0, -1]]
        while heap:
            height, pos = heapq.heappop(heap)
            for i, j in dirs:
                row, col = pos[0] + i, pos[1] + j
                if 0 <= row < n and 0 <= col < m and ref[row][col] == 0:
                    tmp = max(height, heightMap[row][col])
                    result += (tmp - heightMap[row][col])
                    heapq.heappush(heap, [tmp, [row, col]])
                    ref[row][col] = 1
        
        return result