# coding=utf-8

'''
Given a 2d grid map of '1's (land) and '0's (water),
count the number of islands. An island is surrounded by water and
is formed by connecting adjacent lands horizontally or vertically.
You may assume all four edges of the grid are all surrounded by water.

Example 1:

11110
11010
11000
00000
Answer: 1

Example 2:

11000
11000
00100
00011
Answer: 3
'''

'''
此题证明了popleft也是一个代价很高的函数...
其实就是传统的BFS没有任何其他东西
Beat 89.08%
公司：Amazon, Microsoft, Google, Facebook, Zenefits
'''

class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        row = len(grid) - 1
        if row < 0: return 0
        col = len(grid[0]) - 1
        if col < 0: return 0

        count = 0

        for i in xrange(row + 1):
            for j in xrange(col + 1):
                if grid[i][j] == '1':
                    count += 1
                    self.BFS(grid, i, j, row, col)
        return count

    def BFS(self, grid, i, j, row, col):
        store = []
        store.append([i, j])
        while store:
            node = store.pop()
            grid[node[0]][node[1]] = 'a'
            if node[0] - 1 >= 0 and grid[node[0] - 1][node[1]] == '1':
                store.append([node[0] - 1, node[1]])
            if node[0] + 1 <= row and grid[node[0] + 1][node[1]] == '1':
                store.append([node[0] + 1, node[1]])
            if node[1] - 1 >= 0 and grid[node[0]][node[1] - 1] == '1':
                store.append([node[0], node[1] - 1])
            if node[1] + 1 <= col and grid[node[0]][node[1] + 1] == '1':
                store.append([node[0], node[1] + 1])
