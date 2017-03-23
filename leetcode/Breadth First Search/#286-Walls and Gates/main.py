# coding=utf-8

'''
You are given a m x n 2D grid initialized with these three possible values.

-1 - A wall or an obstacle.
0 - A gate.
INF - Infinity means an empty room. We use the value 231 - 1 = 2147483647
to represent INF as you may assume that the distance to a gate is
less than 2147483647.
Fill each empty room with the distance to its nearest gate. If it is
impossible to reach a gate, it should be filled with INF.

For example, given the 2D grid:
INF  -1  0  INF
INF INF INF  -1
INF  -1 INF  -1
  0  -1 INF INF
After running your function, the 2D grid should be:
  3  -1   0   1
  2   2   1  -1
  1  -1   2  -1
  0  -1   3   4
'''

'''
朴素BFS即可，速度上面因为在飞机上不好判断
公司：Google, Facebook
'''

import Queue

class Solution(object):
    def wallsAndGates(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: void Do not return anything, modify rooms in-place instead.
        """
        n = len(rooms)
        if not n:
            return

        m = len(rooms[0])
        if not m:
            return

        gates = []
        for i in xrange(n):
            for j in xrange(m):
                if rooms[i][j] == 0:
                    gates.append([i, j])

        while gates:
            x, y = gates.pop()
            self.BFS(x, y, rooms, n, m)

    def BFS(self, i, j, rooms, n, m):
        queue = Queue.Queue(n * m)
        queue.put([i, j])
        step = [[1, 0], [0, -1], [-1, 0], [0, 1]]

        while not queue.empty():
            x, y = queue.get()
            for i, j in step:
                if x + i >= 0 and x + i < n and y + j >= 0 and \
                    y + j < m and rooms[x + i][y + j] != -1 and \
                    rooms[x][y] + 1 < rooms[x + i][y + j] and \
                    rooms[x + i][y + j] != 0:
                        rooms[x + i][y + j] = rooms[x][y] + 1
                        queue.put([x + i, y + j])
