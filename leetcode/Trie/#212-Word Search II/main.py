# coding=utf-8

'''
Given a 2D board and a list of words from the dictionary, find all words in the board.

Each word must be constructed from letters of sequentially adjacent cell, where "adjacent" cells are 
those horizontally or vertically neighboring. 
The same letter cell may not be used more than once in a word.

For example,
Given words = ["oath","pea","eat","rain"] and board =

[
  ['o','a','a','n'],
  ['e','t','a','e'],
  ['i','h','k','r'],
  ['i','f','l','v']
]
Return ["eat","oath"].
Note:
You may assume that all inputs are consist of lowercase letters a-z.

click to show hint.

You would need to optimize your backtracking to pass the larger test. Could you stop backtracking earlier?

If the current candidate does not exist in all words' prefix, you could stop backtracking immediately. 
What kind of data structure could answer such query efficiently? Does a hash table work? Why or why not? 
How about a Trie? If you would like to learn how to implement a basic trie, please work on this problem: 
Implement Trie (Prefix Tree) first.
'''

'''
实现非常复杂的一道题，需要DFS矩阵的情况下同时DFS Trie树来搜索
1.此题必须先依据set过后的words建立一个Trie树
2.遍历矩阵的每一个字母来收集在Trie树中DFS找到的词
3.搜索问题都必须有的一个checker来进行搜索查重（这里还是用课上介绍的技巧将2D扁平化为1D数组）
4.收集词的容器也是set（避免二次查重）
5.这题真鸡儿难啊...
Beat 82.61%
公司：Microsoft, Airbnb, Google
'''

class Solution(object):
    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        n = len(board)
        if not n:
            return []
        
        m = len(board[0])
        if not m:
            return []

        words = set(words)
        root = {}
        result = set([])
        checker = [0] * (n * m)
        
        for word in words:
            self.insert(root, word)
        
        for i in xrange(n):
            for j in xrange(m):
                if root.has_key(board[i][j]):
                    self.DFS(n, m, 
                            i, j, 
                            board, 
                            root[board[i][j]], 
                            result,
                            checker,
                            [board[i][j]])
        
        return list(result)
        
    def insert(self, root, string):
        cur = root
        for char in string:
            cur = cur.setdefault(char, {})
        cur['#'] = {}

    def DFS(self, n, m, i, j, board, root, result, checker, tmp):
        uni_id = i * m + j
        checker[uni_id] = 1
        if root.has_key('#'):
            result.add(''.join(tmp))
            if len(root.keys()) == 1:
                checker[uni_id] = 0
                return 
        
        dirs = [[0, 1], [1, 0], [-1, 0], [0, -1]]
        for row, col in dirs:
            tmp_row, tmp_col = row + i, col + j
            cur_id = tmp_row * m + tmp_col
            if 0 <= tmp_row < n and 0 <= tmp_col < m and not checker[cur_id]:
                cur_char = board[tmp_row][tmp_col]
                if root.has_key(cur_char):
                    tmp.append(cur_char)
                    self.DFS(n, m, tmp_row, tmp_col, board, root[cur_char], result, checker, tmp)
                    tmp.pop()
        
        checker[uni_id] = 0