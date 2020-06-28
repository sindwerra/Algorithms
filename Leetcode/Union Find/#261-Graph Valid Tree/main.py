# coding=utf-8

'''
Given n nodes labeled from 0 to n - 1 and a list of undirected edges
(each edge is a pair of nodes), write a function to check whether
these edges make up a valid tree.

For example:

Given n = 5 and edges = [[0, 1], [0, 2], [0, 3], [1, 4]], return true.

Given n = 5 and edges = [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]],
return false.

Hint:

Given n = 5 and edges = [[0, 1], [1, 2], [3, 4]], what should your
return? Is this case a valid tree?
According to the definition of tree on Wikipedia: “a tree is an
undirected graph in which any two vertices are connected by exactly
one path. In other words, any connected graph without simple cycles
is a tree.”
Note: you can assume that no duplicate edges will appear in edges.
Since all edges are undirected, [0, 1] is the same as [1, 0] and
thus will not appear together in edges.
'''

'''
注意这里说的是树不是二叉树，所以可以用Union Find算法来证明，且对于一棵树来说，
要求只有三点，有正好n-1条无向边，且内部不存在环，只有一个节点的parent node的父节
点为-1，则为一棵树。当然Union Find肯定也是最慢的判断方法。
Beat 4.37%
公司：Google, Facebook, Zenefits
'''

class Solution(object):
    def validTree(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: bool
        """
        parent = [-1] * n
        count = 0
        head = 0

        for st, ed in edges:
            count += 1

            while parent[st] != -1:
                st = parent[st]
            a = st
            while parent[ed] != -1:
                ed = parent[ed]
            b = ed
            if a != b:
                parent[a] = b
                head = b

        if count != n - 1:
            return False

        for key in xrange(n):
            while parent[key] != -1:
                key = parent[key]
            if key != head:
                return False

        return True
