# coding=utf-8

# '''
# Given a binary tree, return all root-to-leaf paths.
#
# For example, given the following binary tree:
#
#    1
#  /   \
# 2     3
#  \
#   5
# All root-to-leaf paths are:
#
# ["1->2->5", "1->3"]
# '''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {string[]}
    def binaryTreePaths(self, root):
        result = []
        temp = []
        self.BTP(result, temp, root)
        return result

        # 借用假reference结构完成功能

    def BTP(self, lst, sublst, root):
        if root == None: return
        if root.left == None and root.right == None:
            sublst.append(str(root.val))
            one = "->".join(sublst)
            sublst.pop()          # 添加了此元素之后再把它pop出来以上溯
            lst.append(one)
            return

        sublst.append(str(root.val))
        self.BTP(lst, sublst, root.left)
        self.BTP(lst, sublst, root.right)
        sublst.pop()             # 此元素的左树和右树完成遍历后要将此元素pop出来
        return
