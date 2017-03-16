# coding=utf

'''
Given a binary search tree with non-negative values,
find the minimum absolute difference between values of any
two nodes.

Example:

Input:

   1
    \
     3
    /
   2

Output:
1

Explanation:
The minimum absolute difference is 1, which is the difference
between 2 and 1 (or between 2 and 3).
Note: There are at least two nodes in this BST.
'''

'''
中序遍历找最小差值就行
Beat 100%
公司：Google
'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def getMinimumDifference(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        stack = []
        res = sys.maxint
        pre = None
        while root or stack:
            if root:
                stack.append(root)
                root = root.left
            else:
                root = stack.pop()
                if pre and abs(pre.val - root.val) < res:
                    res = abs(pre.val - root.val)
                pre = root
                root = root.right
        return res
