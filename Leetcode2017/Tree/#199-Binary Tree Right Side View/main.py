# coding=utf-8

'''
Given a binary tree, imagine yourself standing on the right side of it,
return the values of the nodes you can see ordered from top to bottom.

For example:
Given the following binary tree,
   1            <---
 /   \
2     3         <---
 \     \
  5     4       <---
You should return [1, 3, 4].
'''

'''
二叉树的层级遍历只取最后一个点即搞定，Beat 95.59%
'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root == None: return []
        res = []
        tmp = 0
        cur, nxt = collections.deque([root]), collections.deque([])
        while len(cur):
            node = cur.pop()
            if node:
                tmp = node.val
                if node.left:
                    nxt.appendleft(node.left)
                if node.right:
                    nxt.appendleft(node.right)
            if len(cur) == 0:
                res.append(tmp)
                cur, nxt = nxt, cur
        return res

'''
另外一种方法
'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def helper(self, root, level, maxLevel, lst):
        if not root:
            return
        if level > maxLevel[0]:
            lst.append(root.val)
            maxLevel[0] = level

        self.helper(root.right, level + 1, maxLevel, lst)
        self.helper(root.left, level + 1, maxLevel, lst)

    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        self.helper(root, 1, [0], res)
        return res
