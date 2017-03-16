# coding=utf-8

'''
Given a 2D board and a word, find if the word exists in the grid.

The word can be constructed from letters of sequentially adjacent cell,
where "adjacent" cells are those horizontally or vertically neighboring.
The same letter cell may not be used more than once.

For example,
Given board =

[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]
word = "ABCCED", -> returns true,
word = "SEE", -> returns true,
word = "ABCB", -> returns false.
'''

'''
DFS,坑太多了，参考矩阵是必须要的，而且每次DFS完之后都必须把参考值清零
避免另外一个点的DFS产生误判，以上例参考ABCCEDA这个字符串的寻找过程
Beat 91.68%
公司：Microsoft, Bloomberg, Facebook
'''

class Solution(object):
    def DFS(self, node, step, word, board, n, m, limit, ref):
        if step == limit:
            return True
        ref[node[0]][node[1]] = 1
        a, b, c, d = False, False, False, False
        if node[0] - 1 >= 0 and word[step + 1] == board[node[0] - 1][node[1]] and ref[node[0] - 1][node[1]] == 0:
            a = self.DFS([node[0] - 1, node[1]], step + 1, word, board, n, m, limit, ref)
            if a: return True
        if node[1] - 1 >= 0 and word[step + 1] == board[node[0]][node[1] - 1] and ref[node[0]][node[1] - 1] == 0:
            b = self.DFS([node[0], node[1] - 1], step + 1, word, board, n, m, limit, ref)
            if b: return True
        if node[0] + 1 < n and word[step + 1] == board[node[0] + 1][node[1]] and ref[node[0] + 1][node[1]] == 0:
            c = self.DFS([node[0] + 1, node[1]], step + 1, word, board, n, m, limit, ref)
            if c: return True
        if node[1] + 1 < m and word[step + 1] == board[node[0]][node[1] + 1] and ref[node[0]][node[1] + 1] == 0:
            d = self.DFS([node[0], node[1] + 1], step + 1, word, board, n, m, limit, ref)
            if d: return True
        ref[node[0]][node[1]] = 0
        return a or b or c or d


    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        stack = []
        n = len(board)
        if not n:
            return False
        m = len(board[0])
        if not m:
            return False

        ref = [([0] * m) for _ in range(n)]

        for i in range(n):
            for j in range(m):
                if board[i][j] == word[0]:
                    stack.append([i, j])

        while stack:
            node = stack.pop()
            res = self.DFS(node, 0, word, board, n, m, len(word) - 1 ,ref)
            if res:
                return True
        return False
