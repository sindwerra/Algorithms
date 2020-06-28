# coding=utf-8

'''
Given a binary tree, return the zigzag level order traversal of
its nodes' values. (ie, from left to right, then right to left for
the next level and alternate between).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its zigzag level order traversal as:
[
  [3],
  [20,9],
  [15,7]
]
'''

'''
也是层级遍历的问题变形，多一个变量记下这是第几层再决定翻不翻转当前list就行了，Beat 97.15%
'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root == None: return []
        cur, nxt = collections.deque([root]), collections.deque([])
        res, tmp = [], []
        count = 0
        while len(cur):
            node = cur.pop()
            if node:
                tmp.append(node.val)
                if node.left:
                    nxt.appendleft(node.left)
                if node.right:
                    nxt.appendleft(node.right)
            if len(cur) == 0:
                if count % 2:
                    tmp.reverse()
                res.append(tmp)
                tmp = []
                cur, nxt = nxt, cur
                count += 1
        return res
