# coding=utf-8

'''
For a undirected graph with tree characteristics, we can choose any node as the root. 
The result graph is then a rooted tree. Among all possible rooted trees, those with
 minimum height are called minimum height trees (MHTs). Given such a graph, write a 
 function to find all the MHTs and return a list of their root labels.

Format
The graph contains n nodes which are labeled from 0 to n - 1. You will be given the number n 
and a list of undirected edges (each edge is a pair of labels).

You can assume that no duplicate edges will appear in edges. Since all edges are undirected, 
[0, 1] is the same as [1, 0] and thus will not appear together in edges.

Example 1:

Given n = 4, edges = [[1, 0], [1, 2], [1, 3]]

        0
        |
        1
       / \
      2   3
return [1]

Example 2:

Given n = 6, edges = [[0, 3], [1, 3], [2, 3], [4, 3], [5, 4]]

     0  1  2
      \ | /
        3
        |
        4
        |
        5
return [3, 4]
'''

'''
gitbook上详述
公司：Google
'''

class Solution(object):
    def findMinHeightTrees(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        if n <= 2:
            return [x for x in xrange(n)]
        
        ind = [set([]) for _ in xrange(n)]

        for st, ed in edges:
            ind[st].add(ed)
            ind[ed].add(st)

        lefts = [x for x in xrange(n) if len(ind[x]) == 1]
        
        while n > 2:
            n -= len(lefts)
            new_lefts = []
            for leave in lefts:
                tmp = ind[leave].pop()
                ind[tmp].remove(leave)
                if len(ind[tmp]) == 1:
                    new_lefts.append(tmp)
            lefts = new_lefts

        return lefts