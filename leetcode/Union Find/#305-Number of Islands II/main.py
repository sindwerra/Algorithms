# coding=utf-8

'''
A 2d grid map of m rows and n columns is initially filled with water. We may perform an addLand operation which turns the water at position (row, col) into a land. Given a list of positions to operate, count the number of islands after each addLand operation. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

Example:

Given m = 3, n = 3, positions = [[0,0], [0,1], [1,2], [2,1]].
Initially, the 2d grid grid is filled with water. (Assume 0 represents water and 1 
represents land).

0 0 0
0 0 0
0 0 0
Operation #1: addLand(0, 0) turns the water at grid[0][0] into a land.

1 0 0
0 0 0   Number of islands = 1
0 0 0
Operation #2: addLand(0, 1) turns the water at grid[0][1] into a land.

1 1 0
0 0 0   Number of islands = 1
0 0 0
Operation #3: addLand(1, 2) turns the water at grid[1][2] into a land.

1 1 0
0 0 1   Number of islands = 2
0 0 0
Operation #4: addLand(2, 1) turns the water at grid[2][1] into a land.

1 1 0
0 0 1   Number of islands = 3
0 1 0
We return the result as an array: [1, 1, 2, 3]

Challenge:

Can you do it in time complexity O(k log mn), where k is the length of the positions?
'''

'''
利用字典的性质来实现并查集，同时要注意一个点的四邻有多个岛屿且当前未联通的情况
速度很慢, Beat 10.07%, lintcode又是MLE...
公司：Google
'''

class Solution(object):
    def numIslands2(self, m, n, positions):
        """
        :type m: int
        :type n: int
        :type positions: List[List[int]]
        :rtype: List[int]
        """
        parent = {}
        result = []
        cur_count = 0

        for position in positions:
            row, col = position
            if 0 <= row < m and 0 <= col < n:
                if not parent:
                    parent[(row, col)] = [-1, -1]
                    cur_count += 1
                else:
                    cur_count = self.searchAndCount(row, 
                                                    col, 
                                                    parent, 
                                                    cur_count,
                                                    m,
                                                    n)
                result.append(cur_count)
        
        return result

    def searchAndCount(self, row, col, parent, cur_count, m, n):
        dirs = [[0, 1], [0, -1], [-1, 0], [1, 0]]
        stack = []
        for dir in dirs:
            tmp_row, tmp_col = row + dir[0], col + dir[1]
            tp = (tmp_row, tmp_col)
            if 0 <= tmp_row < m and 0 <= tmp_col < n:
                if parent.has_key(tp):
                    while parent[tp] != [-1, -1]:
                        tp = (parent[tp][0], parent[tp][1])
                    if tp in stack:
                        continue
                    stack.append(tp)
        
        while len(stack) > 1:
            parent[stack[-1]] = [stack[-2][0], stack[-2][1]]
            cur_count -= 1
            stack.pop()
        
        if not stack:
            parent[(row, col)] = [-1, -1]
            cur_count += 1
        else:
            parent[(row, col)] = [stack[0][0], stack[0][1]]
        
        return cur_count
