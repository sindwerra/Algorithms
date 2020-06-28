# coding=utf-8

'''
Given a non-empty binary search tree and a target value,
find the value in the BST that is closest to the target.

Note:
Given target value is a floating point.
You are guaranteed to have only one unique value in the
BST that is closest to the target.
'''

'''
可以在递归方法中直接判断的，比中序遍历所有节点肯定要快，Beat 54.75%
'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def closestValue(self, root, target):
        """
        :type root: TreeNode
        :type target: float
        :rtype: int
        """
        cls, res = sys.maxint, None
        stack = []
        while root or stack:
            if root:
                stack.append(root)
                root = root.left
            else:
                root = stack.pop()
                ref = abs(target - root.val)
                if ref < cls:
                    res = root.val
                    cls = ref
                root = root.right
        return res
