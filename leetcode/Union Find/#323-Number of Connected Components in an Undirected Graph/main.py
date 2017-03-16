# coding=utf-8

'''
Given n nodes labeled from 0 to n - 1 and a list of undirected edges
(each edge is a pair of nodes), write a function to find the number
of connected components in an undirected graph.

Example 1:
     0          3
     |          |
     1 --- 2    4
Given n = 5 and edges = [[0, 1], [1, 2], [3, 4]], return 2.

Example 2:
     0           4
     |           |
     1 --- 2 --- 3
Given n = 5 and edges = [[0, 1], [1, 2], [2, 3], [3, 4]], return 1.

Note:
You can assume that no duplicate edges will appear in edges.
Since all edges are undirected, [0, 1] is the same as [1, 0] and
thus will not appear together in edges.
'''

'''
相当于把Union-Find算法原原本本的implement一遍，下面是易于理解的版本，
把功能函数都分开了,时间复杂度O(ElgV)
公司：Google, Twitter
'''

class Solution(object):
    def findParent(self, parent, node):
        if parent[node] == -1:
            return node
        else:
            return self.findParent(parent, parent[node])

    def union(self, parent, start, end):
        a = self.findParent(parent, start)
        b = self.findParent(parent, end)
        parent[a] = b

    def countComponents(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        res = 0
        store = {}
        for start, end in edges:
            tmp = store.setdefault(start, [])
            store[start].append(end)

        parent = [-1] * n

        for key in store:
            for val in store[key]:
                a = self.findParent(parent, key)
                b = self.findParent(parent, val)
                if a != b:
                    self.union(parent, a, b)

        for s in parent:
            if s == -1:
                res += 1
        return res

'''
代码简化版，把所有函数都放到一起了
'''

class Solution(object):
    def countComponents(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        res = n
        parent = [-1] * n

        for lst in edges:
            while parent[lst[0]] != -1:
                lst[0] = parent[lst[0]]
            a = lst[0]
            while parent[lst[1]] != -1:
                lst[1] = parent[lst[1]]
            b = lst[1]
            if a != b:
                parent[a] = b
                res -= 1

        return res


'''
下面是DFS的做法，速度快很多，时间复杂度是O(V+E)
Beat 92.33%
'''

class Solution(object):
    def DFS_visit(self, key, color, store):
        color[key] = 1
        for node in store[key]:
            if not color[node]:
                self.DFS_visit(node, color, store)
        color[key] = 2

    def countComponents(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        store = {}
        for start, end in edges:
            store.setdefault(start, [])
            store[start].append(end)
            store.setdefault(end, [])
            store[end].append(start)

        color = [0] * n
        res = 0

        for key in xrange(n):
            if not store.has_key(key):
                res += 1
                continue

            if not color[key]:
                self.DFS_visit(key, color, store)
                res += 1
        return res
