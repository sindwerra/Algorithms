# coding=utf-8

'''
Given a 2D board containing 'X' and 'O' (the letter O), 
capture all regions surrounded by 'X'.

A region is captured by flipping all 'O's into 'X's in that surrounded region.

For example,
X X X X
X O O X
X X O X
X O X X
After running your function, the board should be:

X X X X
X X X X
X X X X
X O X X
'''

'''
这里用的BFS做法，但是代码太过冗余了，beacon和BFS两个函数基本上是一样的，
只是BFS需要改board矩阵而beacon函数不用改而已，总的逻辑是先巡视四边，四边
有'O'出现则从这里调用beacon函数BFS然后标记所有途径过的O用ref标记起来
然后再用BFS遍历其他中间点，一旦是O且不是和四边相连的O则改为X
Beat 45.66% 应该可以用并查集达到更快速度
'''

class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        n = len(board)
        if not n:
            return 

        m = len(board[0])
        if not m:
            return 

        ref = [([0] * m) for _ in xrange(n)]
        for i in xrange(n):
            if board[i][0] == 'O' and ref[i][0] == 0 :
                self.beacon(board, ref, i, 0, n, m)
            if board[i][m - 1] == 'O' and ref[i][m - 1] == 0:
                self.beacon(board, ref, i, m - 1, n, m)
        for i in xrange(m):
            if board[0][i] == 'O' and ref[0][i] == 0:
                self.beacon(board, ref, 0, i, n, m)
            if board[n - 1][i] == 'O' and ref[n - 1][i] == 0:
                self.beacon(board, ref, n - 1, i, n, m)

        for i in xrange(1, n - 1):
            for j in xrange(1, m - 1):
                if board[i][j] == 'O' and ref[i][j] == 0:
                    self.BFS(board, ref, i, j, n, m)

    
    def beacon(self, board, ref, i, j, n, m):
        q = collections.deque([[i, j]])
        
        dirs =  [[0, 1], [1, 0], [-1, 0], [0, -1]]

        while q:
            row, col = q.pop()
            ref[i][j] = 1
            for i, j in dirs:
                tmp_row, tmp_col = i + row, j + col
                if 0 <= tmp_row < n and 0 <= tmp_col < m:
                    if board[tmp_row][tmp_col] == 'O' and ref[tmp_row][tmp_col] == 0:
                        ref[tmp_row][tmp_col] = 1
                        q.appendleft([tmp_row, tmp_col])
                        
        
    def BFS(self, board, ref, i, j, n, m):
        q = collections.deque([[i, j]])
        
        dirs =  [[0, 1], [1, 0], [-1, 0], [0, -1]]

        while q:
            row, col = q.pop()
            board[row][col] = 'X'
            ref[i][j] = 1
            for i, j in dirs:
                tmp_row, tmp_col = i + row, j + col
                if 0 <= tmp_row < n and 0 <= tmp_col < m:
                    if board[tmp_row][tmp_col] == 'O' and ref[tmp_row][tmp_col] == 0:
                        ref[tmp_row][tmp_col] = 1
                        q.appendleft([tmp_row, tmp_col])