# coding=utf-8

'''
Clone an undirected graph. Each node in the graph contains a label
and a list of its neighbors.


OJ's undirected graph serialization:
Nodes are labeled uniquely.

We use # as a separator for each node, and , as a separator for node label
and each neighbor of the node.
As an example, consider the serialized graph {0,1,2#1,2#2,2}.

The graph has a total of three nodes, and therefore contains three parts
as separated by #.

First node is labeled as 0. Connect node 0 to both nodes 1 and 2.
Second node is labeled as 1. Connect node 1 to node 2.
Third node is labeled as 2. Connect node 2 to node 2 (itself),
thus forming a self-cycle.
Visually, the graph looks like the following:

       1
      / \
     /   \
    0 --- 2
         / \
         \_/
'''

'''
BFS即可，总体分三步走，先把每一个点都复制出来，再用一个哈希表与原节点连接起来
最后利用这个哈希表将所有edges连起来,Beat 97.14%
公司：Pocket Gems, Google, Uber, Facebook
'''

# Definition for a undirected graph node
# class UndirectedGraphNode:
#     def __init__(self, x):
#         self.label = x
#         self.neighbors = []

class Solution:
    # @param node, a undirected graph node
    # @return a undirected graph node
    def cloneGraph(self, node):
        if not node:
            return None

        hash_table = {}
        tmp = [node]
        ref = {}

        while tmp:
            pt = tmp.pop()
            ref[pt] = 1
            hash_table[pt] = UndirectedGraphNode(pt.label)

            for key in pt.neighbors:
                if ref.has_key(key):
                    continue
                tmp.append(key)

        for key in hash_table:
            for pt in key.neighbors:
                hash_table[key].neighbors.append(hash_table[pt])

        return hash_table[node]
        
