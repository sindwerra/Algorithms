# coding=utf-8

'''
You want to build a house on an empty land which reaches all buildings in the 
shortest amount of distance. 
You can only move up, down, left and right. You are given a 2D grid of values 0, 1 or 2, where:

Each 0 marks an empty land which you can pass by freely.
Each 1 marks a building which you cannot pass through.
Each 2 marks an obstacle which you cannot pass through.
For example, given three buildings at (0,0), (0,4), (2,2), and an obstacle at (0,2):

1 - 0 - 2 - 0 - 1
|   |   |   |   |
0 - 0 - 0 - 0 - 0
|   |   |   |   |
0 - 0 - 1 - 0 - 0
The point (1,2) is an ideal empty land to build a house, as the total travel 
distance of 3+3+1=7 is minimal. So return 7.

Note:
There will be at least one building. If it is not possible to build such house according 
to the above rules, return -1.
'''

'''
这道题过的条件比较苛刻，必须用一个reacable_count的matrix记录每个点被BFS扫到几次
如果不是所有的邮局都能扫到这个点则此处的距离没有意义。
Beat 33.50%
公司：Google, Zenefits
'''

class Solution(object):
    def shortestDistance(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        n = len(grid)
        if not n:
            return -1
        
        m = len(grid[0])
        if not m:
            return -1

        distance = [([0] * m) for _ in range(n)]
        reachable_count = [([0] * m) for _ in range(n)]

        count_building = 0
        
        for i in xrange(n):
            for j in xrange(m):
                if grid[i][j] == 1:
                    distance[i][j] = sys.maxint
                    self.BFS(i, j, distance, n, m, grid, reachable_count)
                    count_building += 1

        res = sys.maxint

        for i in xrange(n):
            for j in xrange(m):
                if distance[i][j] < res and reachable_count[i][j] == count_building:
                    res = distance[i][j]
        
        return res if res != sys.maxint else -1

    def BFS(self, i, j, distance, n, m, grid, reachable_count):
        ref = [([sys.maxint] * m) for _ in range(n)]
        q = collections.deque([[i, j]])
        ref[i][j] = 0
        step = [[1, 0], [0, 1], [-1, 0], [0, -1]]

        while q:
            x, y = q.pop()
            for row, col in step:
                if x + row < n and x + row >= 0 and y + col < m and y + col >= 0 and \
                    grid[x + row][y + col] == 0 and ref[x][y] + 1 < ref[x + row][y + col]:
                        ref[x + row][y + col] = ref[x][y] + 1
                        q.appendleft([x + row, y + col])
            distance[x][y] += ref[x][y]
            reachable_count[x][y] += 1