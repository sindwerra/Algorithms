# coding=utf-8

'''
Given a binary tree, determine if it is height-balanced.

For this problem, a height-balanced binary tree is defined as a
binary tree in which the depth of the two subtrees of every node
never differ by more than 1.
'''

'''
一棵树是否平衡取决于三点，左子树是否平衡，右子树是否平衡，以及左右子树高差是否小于等于1
这里用一个辅助函数height来帮助判断，返回一个包含高度以及此点的为根节点的树是否平衡的tuple
Beat 61.75%
'''


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def height(self, root):
        if root == None: return (0, True)
        lh = self.height(root.left)
        rh = self.height(root.right)
        return (max(lh[0], rh[0]) + 1, abs(lh[0] - rh[0]) <= 1 and lh[1] and rh[1])

    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root == None: return True
        lf = self.height(root.left)
        rt = self.height(root.right)
        return (abs(lf[0] - rt[0]) <= 1) and lf[1] and rt[1]
