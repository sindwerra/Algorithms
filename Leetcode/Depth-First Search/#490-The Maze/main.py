# coding=utf-8

'''
There is a ball in a maze with empty spaces and walls. The ball can go through empty spaces by rolling up, down, left or right, but it won't stop rolling until hitting a wall. When the ball stops, it could choose the next direction.

Given the ball's start position, the destination and the maze, determine whether the ball could stop at the destination.

The maze is represented by a binary 2D array. 1 means the wall and 0 means the empty space. You may assume that the borders of the maze are all walls. The start and destination coordinates are represented by row and column indexes.

Example 1

Input 1: a maze represented by a 2D array

0 0 1 0 0
0 0 0 0 0
0 0 0 1 0
1 1 0 1 1
0 0 0 0 0

Input 2: start coordinate (rowStart, colStart) = (0, 4)
Input 3: destination coordinate (rowDest, colDest) = (4, 4)

Output: true
Explanation: One possible way is : left -> down -> left -> down -> right -> down -> right.

Example 2

Input 1: a maze represented by a 2D array

0 0 1 0 0
0 0 0 0 0
0 0 0 1 0
1 1 0 1 1
0 0 0 0 0

Input 2: start coordinate (rowStart, colStart) = (0, 4)
Input 3: destination coordinate (rowDest, colDest) = (3, 2)

Output: false
Explanation: There is no way for the ball to stop at the destination.

'''

'''
这道题就是在BFS的外皮下包了一个DFS，每个点都可以朝四个方向直到碰壁（可能是四边，也可能是区域内的凸起）
然后参考矩阵在这里只用记录停留点的重复就行了，球滚过但不会停下的点不用标记（因为可能有比较复杂的方法
到达终点，需多次经过一个中间点）
Beat 90.00%
公司：Google
'''

class Solution(object):
    def hasPath(self, maze, start, destination):
        """
        :type maze: List[List[int]]
        :type start: List[int]
        :type destination: List[int]
        :rtype: bool
        """
        n = len(maze)
        if not n:
            return False
        
        m = len(maze[0])
        if not m:
            return False
        
        ref = [([0] * m) for _ in xrange(n)]
        ref[start[0]][start[1]] = 1
        dirs = [[0, 1], [1, 0], [-1, 0], [0, -1]]

        q = collections.deque([[start[0], start[1]]])
        while q:
            node = q.pop()
            if node == destination:
                return True
            for i, j in dirs:
                self.DFS(i, j, node, q, ref, maze, n, m)
        
        return False

    def DFS(self, i, j, node, q, ref, maze, n, m):
        row, col = node
        while 0 <= row + i < n and 0 <= col + j < m and maze[row + i][col + j] != 1:
            row += i
            col += j
        if maze[row][col] == 0 and ref[row][col] == 0:
            ref[row][col] = 1
            q.appendleft([row, col])