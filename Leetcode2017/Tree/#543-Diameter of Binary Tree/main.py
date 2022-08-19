# coding=utf-8

'''
Given a binary tree, you need to compute the length of the diameter of the tree. 
The diameter of a binary tree is the length of the longest path between any two 
nodes in a tree. This path may or may not pass through the root.

Example:
Given a binary tree 
          1
         / \
        2   3
       / \     
      4   5    
Return 3, which is the length of the path [4,2,1,3] or [5,2,1,3].

Note: The length of path between two nodes is represented by the number of edges between them.
'''

'''
标准Divide and Conquer,返回一个tuple，第一个值是当前点最长diameter，第二个点是带上此节点的最长半边路径（或左或右）
Beat 96.69%
公司：Google, Facebook
'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        
        return self.helper(root)[0] - 1

    def helper(self, root):
        if not root:
            return (0, 0)
        
        left = self.helper(root.left)
        right = self.helper(root.right)

        return (max(left[0], right[0], left[1] + right[1] + 1), max(left[1], right[1]) + 1)