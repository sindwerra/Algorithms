# coding=utf-8

'''
Given an 2D board, count how many different battleships are in it.
The battleships are represented with 'X's,
empty slots are represented with '.'s. You may assume the following rules:

You receive a valid board, made of only battleships or empty slots.
Battleships can only be placed horizontally or vertically. In other words,
they can only be made of the shape 1xN (1 row, N columns) or Nx1 (N rows,
1 column), where N can be of any size.
At least one horizontal or vertical cell separates between
two battleships - there are no adjacent battleships.
Example:
X..X
...X
...X
In the above board there are 2 battleships.
Invalid Example:
...X
XXXX
...X
This is an invalid board that you will not receive - as battleships
will always have a cell separating between them.
Follow up:
Could you do it in one-pass, using only O(1) extra memory and without
modifying the value of the board?
'''

# 跟孤岛问题其实一模一样，都是BFS解决，不过不改变矩阵的情况O（1）空间一遍解决的方法没有想出来
# Beat 64.97%

class Solution(object):
    def countBattleships(self, board):
        """
        :type board: List[List[str]]
        :rtype: int
        """
        count = 0
        n = len(board)
        if n == 0: return 0
        m = len(board[0])
        if m == 0: return 0

        for row in xrange(n):
            for col in xrange(m):
                if board[row][col] == 'X':
                    count += 1
                    self.BFS(board, row, col, n, m)
        return count

    def BFS(self, board, row, col, n, m):
        store = [[row, col]]
        board[row][col] == 'A'
        while len(store) != 0:
            node = store.pop(0)
            c, l = node[0], node[1]
            if c - 1 >= 0 and board[c - 1][l] == 'X':
                board[c - 1][l] = 'A'
                store.append([c - 1, l])
            if c + 1 <= n - 1 and board[c + 1][l] == 'X':
                board[c + 1][l] = 'A'
                store.append([c + 1, l])
            if l - 1 >= 0 and board[c][l - 1] == 'X':
                board[c][l - 1] = 'A'
                store.append([c, l - 1])
            if l + 1 <= m - 1 and board[c][l + 1] == 'X':
                board[c][l + 1] = 'A'
                store.append([c, l + 1])
