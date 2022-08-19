# coding=utf-8

'''
Let's play the minesweeper game (Wikipedia, online game)!

You are given a 2D char matrix representing the game board.
'M' represents an unrevealed mine, 'E' represents an unrevealed
 empty square, 'B' represents a revealed blank square that has
no adjacent (above, below, left, right, and all 4 diagonals)
mines, digit ('1' to '8') represents how many mines are
adjacent to this revealed square, and finally 'X' represents
a revealed mine.

Now given the next click position (row and column indices)
among all the unrevealed squares ('M' or 'E'), return the
board after revealing this position according to the following
rules:

If a mine ('M') is revealed, then the game is over - change
it to 'X'.
If an empty square ('E') with no adjacent mines is revealed,
then change it to revealed blank ('B') and all of its adjacent
unrevealed squares should be revealed recursively.
If an empty square ('E') with at least one adjacent mine is
revealed, then change it to a digit ('1' to '8') representing
the number of adjacent mines.
Return the board when no more squares will be revealed.
Example 1:
Input:

[['E', 'E', 'E', 'E', 'E'],
 ['E', 'E', 'M', 'E', 'E'],
 ['E', 'E', 'E', 'E', 'E'],
 ['E', 'E', 'E', 'E', 'E']]

Click : [3,0]

Output:

[['B', '1', 'E', '1', 'B'],
 ['B', '1', 'M', '1', 'B'],
 ['B', '1', '1', '1', 'B'],
 ['B', 'B', 'B', 'B', 'B']]

Explanation:

Example 2:
Input:

[['B', '1', 'E', '1', 'B'],
 ['B', '1', 'M', '1', 'B'],
 ['B', '1', '1', '1', 'B'],
 ['B', 'B', 'B', 'B', 'B']]

Click : [1,2]

Output:

[['B', '1', 'E', '1', 'B'],
 ['B', '1', 'X', '1', 'B'],
 ['B', '1', '1', '1', 'B'],
 ['B', 'B', 'B', 'B', 'B']]

Explanation:

Note:
The range of the input matrix's height and width is [1,50].
The click position will only be an unrevealed square ('M' or
'E'), which also means the input board contains at least one
clickable square.
The input board won't be a stage when game is over (some mines
 have been revealed).
For simplicity, not mentioned rules should be ignored in this
problem. For example, you don't need to reveal all the
unrevealed mines when the game is over, consider any cases
that you will win the game or flag any squares.
'''

'''
就是扫雷游戏，估计是写过最长的代码了，用了一个ref矩阵再加上flag矩阵，
BFS算法，速度太慢了可以优化
Beat 11.84%
公司：Amazon
'''

class Solution(object):
    def updateBoard(self, board, click):
        """
        :type board: List[List[str]]
        :type click: List[int]
        :rtype: List[List[str]]
        """
        n = len(board)
        if not n:
            return []
        m = len(board[0])
        if not m:
            return []

        ref = [([0] * m) for _ in range(n)]
        for i in range(n):
            for j in range(m):
                tmp = 0
                if board[i][j] == 'M':
                    ref[i][j] = 'X'
                elif board[i][j] == 'E':
                    if i - 1 >= 0 and board[i - 1][j] == 'M':
                        tmp += 1
                    if i - 1 >= 0 and j - 1 >= 0 and board[i - 1][j - 1] == 'M':
                        tmp += 1
                    if i - 1 >= 0 and j + 1 < m and board[i - 1][j + 1] == 'M':
                        tmp += 1
                    if j - 1 >= 0 and board[i][j - 1] == 'M':
                        tmp += 1
                    if j + 1 < m and board[i][j + 1] == 'M':
                        tmp += 1
                    if i + 1 < n and j - 1 >= 0 and board[i + 1][j - 1] == 'M':
                        tmp += 1
                    if i + 1 < n and j + 1 < m and board[i + 1][j + 1] == 'M':
                        tmp += 1
                    if i + 1 < n and board[i + 1][j] == 'M':
                        tmp += 1
                    ref[i][j] = str(tmp) if tmp else 'B'
                else:
                    ref[i][j] = board[i][j]

        flag = [([True] * m) for _ in range(n)]
        queue = collections.deque([click])

        while queue:
            tmp = queue.pop()
            node = board[tmp[0]][tmp[1]]
            if not flag[tmp[0]][tmp[1]]:
                continue
            if node == 'M':
                board[tmp[0]][tmp[1]] = 'X'
                break
            if node == 'E' and ref[tmp[0]][tmp[1]].isdigit():
                board[tmp[0]][tmp[1]] = ref[tmp[0]][tmp[1]]
                flag[tmp[0]][tmp[1]] = False
                continue

            if tmp[0] - 1 >= 0 and board[tmp[0] - 1][tmp[1]] == 'E':
                queue.appendleft([tmp[0] - 1, tmp[1]])

            if tmp[0] - 1 >= 0 and tmp[1] - 1 >= 0 and board[tmp[0] - 1][tmp[1] - 1] == 'E':
                queue.appendleft([tmp[0] - 1, tmp[1] - 1])

            if tmp[0] - 1 >= 0 and tmp[1] + 1 < m and board[tmp[0] - 1][tmp[1] + 1] == 'E':
                queue.appendleft([tmp[0] - 1, tmp[1] + 1])

            if tmp[1] - 1 >= 0 and board[tmp[0]][tmp[1] - 1] == 'E':
                queue.appendleft([tmp[0], tmp[1] - 1])

            if tmp[1] + 1 < m and board[tmp[0]][tmp[1] + 1] == 'E':
                queue.appendleft([tmp[0], tmp[1] + 1])

            if tmp[0] + 1 < n and tmp[1] - 1 >= 0 and board[tmp[0] + 1][tmp[1] - 1] == 'E':
                queue.appendleft([tmp[0] + 1, tmp[1] - 1])

            if tmp[0] + 1 < n and tmp[1] + 1 < m and board[tmp[0] + 1][tmp[1] + 1] == 'E':
                queue.appendleft([tmp[0] + 1, tmp[1] + 1])

            if tmp[0] + 1 < n and board[tmp[0] + 1][tmp[1]] == 'E':
                queue.appendleft([tmp[0] + 1, tmp[1]])

            board[tmp[0]][tmp[1]] = ref[tmp[0]][tmp[1]]
            flag[tmp[0]][tmp[1]] = False

        return board


'''
优化后的算法，取消了ref矩阵
用count_node和count_mine两个值来判断是否要止步
Beat 95.27%
'''

class Solution(object):
    def updateBoard(self, board, click):
        """
        :type board: List[List[str]]
        :type click: List[int]
        :rtype: List[List[str]]
        """
        n = len(board)
        if not n:
            return []
        m = len(board[0])
        if not m:
            return []

        flag = [([True] * m) for _ in range(n)]
        queue = [click]

        while queue:
            tmp = queue.pop()
            if not flag[tmp[0]][tmp[1]]:
                continue
            if board[tmp[0]][tmp[1]] == 'M':
                board[tmp[0]][tmp[1]] = 'X'
                break

            count_mine, count_node = 0, 0

            if tmp[0] - 1 >= 0 and flag[tmp[0] - 1][tmp[1]]:
                if board[tmp[0] - 1][tmp[1]] == 'E':
                    queue.append([tmp[0] - 1, tmp[1]])
                    count_node += 1
                if board[tmp[0] - 1][tmp[1]] == 'M':
                    count_mine += 1

            if tmp[0] - 1 >= 0 and tmp[1] - 1 >= 0 and flag[tmp[0] - 1][tmp[1] - 1]:
                if board[tmp[0] - 1][tmp[1] - 1] == 'E':
                    queue.append([tmp[0] - 1, tmp[1] - 1])
                    count_node += 1
                if board[tmp[0] - 1][tmp[1] - 1] == 'M':
                    count_mine += 1

            if tmp[0] - 1 >= 0 and tmp[1] + 1 < m and flag[tmp[0] - 1][tmp[1] + 1]:
                if board[tmp[0] - 1][tmp[1] + 1] == 'E':
                    queue.append([tmp[0] - 1, tmp[1] + 1])
                    count_node += 1
                if board[tmp[0] - 1][tmp[1] + 1] == 'M':
                    count_mine += 1

            if tmp[1] - 1 >= 0  and flag[tmp[0]][tmp[1] - 1]:
                if board[tmp[0]][tmp[1] - 1] == 'E':
                    queue.append([tmp[0], tmp[1] - 1])
                    count_node += 1
                if board[tmp[0]][tmp[1] - 1] == 'M':
                    count_mine += 1

            if tmp[1] + 1 < m and flag[tmp[0]][tmp[1] + 1]:
                if board[tmp[0]][tmp[1] + 1] == 'E':
                    queue.append([tmp[0], tmp[1] + 1])
                    count_node += 1
                if board[tmp[0]][tmp[1] + 1] == 'M':
                    count_mine += 1

            if tmp[0] + 1 < n and tmp[1] - 1 >= 0 and flag[tmp[0] + 1][tmp[1] - 1]:
                if board[tmp[0] + 1][tmp[1] - 1] == 'E':
                    queue.append([tmp[0] + 1, tmp[1] - 1])
                    count_node += 1
                if board[tmp[0] + 1][tmp[1] - 1] == 'M':
                    count_mine += 1

            if tmp[0] + 1 < n and tmp[1] + 1 < m and flag[tmp[0] + 1][tmp[1] + 1]:
                if board[tmp[0] + 1][tmp[1] + 1] == 'E':
                    queue.append([tmp[0] + 1, tmp[1] + 1])
                    count_node += 1
                if board[tmp[0] + 1][tmp[1] + 1] == 'M':
                    count_mine += 1

            if tmp[0] + 1 < n and flag[tmp[0] + 1][tmp[1]]:
                if board[tmp[0] + 1][tmp[1]] == 'E':
                    queue.append([tmp[0] + 1, tmp[1]])
                    count_node += 1
                if board[tmp[0] + 1][tmp[1]] == 'M':
                    count_mine += 1

            if board[tmp[0]][tmp[1]] == 'E':
                if not count_mine:
                    board[tmp[0]][tmp[1]] = 'B'
                else:
                    board[tmp[0]][tmp[1]] = str(count_mine)
                    while count_node:
                        queue.pop()
                        count_node -= 1
                flag[tmp[0]][tmp[1]] = False
                continue

        return board                        
