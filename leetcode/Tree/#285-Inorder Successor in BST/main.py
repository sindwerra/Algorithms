# coding=utf-8

'''
Given a binary search tree and a node in it,
find the in-order successor of that node in the BST.

Note: If the given node has no in-order successor in the tree, return null.
'''

'''
这题肯定有比变成数组更快的递归遍历方法，待拓展，Beat 18.16%

公司：Pocket Gems， Microsoft， Facebook
'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderSuccessor(self, root, p):
        """
        :type root: TreeNode
        :type p: TreeNode
        :rtype: TreeNode
        """
        stack = []
        res = []
        count, index = 0, 0
        while root or len(stack):
            if root:
                stack.append(root)
                root = root.left
            else:
                root = stack.pop()
                count += 1
                if root == p:
                    index = count
                res.append(root)
                root = root.right
        return res[index] if index < count else None
        
