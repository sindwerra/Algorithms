# coding=utf-8

'''
According to the Wikipedia's article: "The Game of Life, also
known simply as Life, is a cellular automaton devised by the
British mathematician John Horton Conway in 1970."

Given a board with m by n cells, each cell has an initial
state live (1) or dead (0). Each cell interacts with its eight neighbors
(horizontal, vertical, diagonal) using the following four rules
(taken from the above Wikipedia article):

Any live cell with fewer than two live neighbors dies,
as if caused by under-population.
Any live cell with two or three live neighbors
lives on to the next generation.
Any live cell with more than three live neighbors dies,
as if by over-population..
Any dead cell with exactly three live neighbors
becomes a live cell, as if by reproduction.
Write a function to compute the next state (after one update) of
the board given its current state.

Follow up:
Could you solve it in-place? Remember that the board needs to
be updated at the same time: You cannot update some cells first and
then use their updated values to update other cells.
In this question, we represent the board using a 2D array.
In principle, the board is infinite, which would cause problems
when the active area encroaches the border of the array.
How would you address these problems?
'''

# 其实就是BFS，把BFS放到一个函数里面写非常复杂啊...
# In-place的做法其实就是把每个entry从int变成list，存下当前值和下一轮的值
# Beat 96.93%

class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        n = len(board)
        if n == 0: return
        m = len(board[0])
        if m == 0: return

        for a in xrange(n):
            for b in xrange(m):
                board[a][b] = [board[a][b], -1]

        for row in xrange(n):
            for col in xrange(m):
                # BFS记下有多少live neighbor

                count = 0
                left, right, up, down = False, False, False, False
                if row - 1 >= 0: up = True
                if row + 1 <= n - 1: down = True
                if col - 1 >= 0: left = True
                if col + 1 <= m - 1: right = True
                if left:
                    if board[row][col - 1][0] == 1: count += 1
                if right:
                    if board[row][col + 1][0] == 1: count += 1
                if down:
                    if board[row + 1][col][0] == 1: count += 1
                    if left:
                        if board[row + 1][col - 1][0] == 1: count += 1
                    if right:
                        if board[row + 1][col + 1][0] == 1: count += 1
                if up:
                    if board[row - 1][col][0] == 1: count += 1
                    if left:
                        if board[row - 1][col - 1][0] == 1: count += 1
                    if right:
                        if board[row - 1][col + 1][0] == 1: count += 1

                # 判断当前点的下个状态

                if board[row][col][0] == 1:
                    if count < 2: board[row][col][1] = 0
                    elif 2 <= count <= 3: board[row][col][1] = 1
                    elif count > 3: board[row][col][1] = 0
                else:
                    if count == 3: board[row][col][1] = 1
                    else: board[row][col][1] = 0

        # 将矩阵回复原状

        for c in xrange(n):
            for d in xrange(m):
                board[c][d] = board[c][d][1]
