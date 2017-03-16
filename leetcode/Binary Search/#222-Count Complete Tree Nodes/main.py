# coding=utf-8

'''
Given a complete binary tree, count the number of nodes.

Definition of a complete binary tree from Wikipedia:
In a complete binary tree every level, except possibly the last,
is completely filled, and all nodes in the last level are as far left as
possible. It can have between 1 and 2h nodes inclusive at the last level h.
'''

'''
还是靠牛客网看了才做出来...
因为是完全树所以必然是由数个满树组成的
先找到左子树的高，再找到右子树的高
如果两高相等，则必然左子树是满树可以直接计算，右子树继续递归
如果两高不等，则必然右子树是满树可以直接计算，左子树继续递归
最后算出结果
Beat 75.54%
'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findLeft(self, root):
        if not root:
            return 0
        return self.findLeft(root.left) + 1

    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        left = self.findLeft(root.left)
        right = self.findLeft(root.right)
        zuo, you = 0, 0
        if left == right:
            zuo = 2 ** left - 1
            you = self.countNodes(root.right)
        else:
            zuo = 2 ** right - 1
            you = self.countNodes(root.left)
        return zuo + you + 1
