# coding=utf-8

'''
Given inorder and postorder traversal of a tree, construct the binary tree.

Note:
You may assume that duplicates do not exist in the tree.
'''

'''
和inorder&preorder那道题基本一样，不过根节点是在最后一个点，且紧随其后的是
根节点的右孩子结点而不是左孩子结点，逻辑相应做调整就好，Beat 26.86%
肯定有其他思路解这个题
'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        if not inorder: return None
        node = postorder.pop()
        mid = inorder.index(node)
        root = TreeNode(node)
        root.right = self.buildTree(inorder[mid + 1:], postorder)
        root.left = self.buildTree(inorder[:mid], postorder)
        return root
